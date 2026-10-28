"""@file
@brief Selenium adapter for the GamePort, and the factory for the Chrome driver.
"""

import os
from collections.abc import Callable, Mapping
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from cookie_clicker_bot.constants import (
    CHROME_BIN_ENV,
    CHROMEDRIVER_ENV,
    CLICK_RETRIES,
    ELEMENT_TIMEOUT_SECONDS,
)

_HEADLESS_ARGUMENTS: tuple[str, ...] = (
    "--headless=new",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--window-size=1280,1024",
)

_RETRYABLE_ERRORS = (StaleElementReferenceException, ElementClickInterceptedException)


def _retry_on_page_change[T](action: Callable[[], T]) -> T:
    """@brief Run the action again when the game re-renders the page under it.

    The action finds its element itself, so each attempt works on a fresh one.

    @param action Finds the element and acts on it.
    @return What the action returns.
    @throws StaleElementReferenceException When every attempt found a stale element.
    @throws ElementClickInterceptedException When every attempt was blocked.
    """
    attempts_left = CLICK_RETRIES
    while True:
        try:
            return action()
        except _RETRYABLE_ERRORS:
            if attempts_left == 0:
                raise
            attempts_left -= 1


class SeleniumGame:
    """@brief Operates the game page through a Selenium web driver."""

    def __init__(self, driver: WebDriver) -> None:
        """@brief Create the adapter.
        @param driver The web driver to operate; the caller owns its creation.
        """
        self._driver = driver

    def open_page(self, url: str) -> None:
        """@brief Load the page at the address.
        @param url The address of the game.
        """
        self._driver.get(url)

    def wait_for_element(self, element_id: str) -> None:
        """@brief Block until the element is on the page.
        @param element_id The HTML id of the element.
        @throws selenium.common.exceptions.TimeoutException When it never appears.
        """
        _retry_on_page_change(
            lambda: WebDriverWait(self._driver, ELEMENT_TIMEOUT_SECONDS).until(
                expected_conditions.presence_of_element_located((By.ID, element_id))
            )
        )

    def click_element(self, element_id: str) -> None:
        """@brief Click the element with a real click, never a script click.

        The game rate-limits synthetic clicks, so the click must come from the
        browser the way a user's does.

        @param element_id The HTML id of the element.
        @throws selenium.common.exceptions.TimeoutException When it never
            becomes clickable.
        @throws StaleElementReferenceException When the element stays stale
            after CLICK_RETRIES retries.
        """
        _retry_on_page_change(lambda: self._click_once(element_id))

    def _click_once(self, element_id: str) -> None:
        element = WebDriverWait(self._driver, ELEMENT_TIMEOUT_SECONDS).until(
            expected_conditions.element_to_be_clickable((By.ID, element_id))
        )
        element.click()

    def read_text(self, element_id: str) -> str:
        """@brief Return the visible text of the element.
        @param element_id The HTML id of the element.
        @return The text as shown on the page.
        """
        return _retry_on_page_change(
            lambda: self._driver.find_element(By.ID, element_id).text
        )

    def read_attribute(self, element_id: str, attribute: str) -> str:
        """@brief Return an attribute of the element.
        @param element_id The HTML id of the element.
        @param attribute The attribute name, for example "class".
        @return The value, or an empty string when the attribute is absent.
        """
        value = _retry_on_page_change(
            lambda: self._driver.find_element(By.ID, element_id).get_attribute(
                attribute
            )
        )
        return value or ""

    def save_screenshot(self, path: Path) -> None:
        """@brief Save a PNG of the page, creating the parent folder when needed.
        @param path The file to write.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        self._driver.save_screenshot(str(path))

    def close(self) -> None:
        """@brief Quit the browser and end the driver session."""
        self._driver.quit()


def build_chrome_options(
    headless: bool, env: Mapping[str, str]
) -> webdriver.ChromeOptions:
    """@brief Build the Chrome options.
    @param headless True to run without a window, for a container or CI.
    @param env The environment; CHROME_BIN names the Chrome binary when set.
    @return The options for the Chrome driver.
    """
    options = webdriver.ChromeOptions()
    if headless:
        for argument in _HEADLESS_ARGUMENTS:
            options.add_argument(argument)
    chrome_binary = env.get(CHROME_BIN_ENV)
    if chrome_binary:
        options.binary_location = chrome_binary
    return options


def build_chrome_service(env: Mapping[str, str]) -> Service | None:
    """@brief Build the chromedriver service when the environment names one.
    @param env The environment; CHROMEDRIVER names the executable when set.
    @return The service, or None to let Selenium Manager find the driver.
    """
    driver_path = env.get(CHROMEDRIVER_ENV)
    if not driver_path:
        return None
    return Service(executable_path=driver_path)


def create_chrome_driver(headless: bool = False) -> WebDriver:
    """@brief Build a Chrome web driver.
    @param headless True to run without a window, for a container or CI.
    @return The started Chrome driver.
    """
    options = build_chrome_options(headless, os.environ)
    service = build_chrome_service(os.environ)
    if service is None:
        return webdriver.Chrome(options=options)
    return webdriver.Chrome(options=options, service=service)
