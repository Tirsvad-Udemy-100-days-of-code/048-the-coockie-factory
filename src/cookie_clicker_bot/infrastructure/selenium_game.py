"""@file
@brief Selenium adapter for the GamePort, and the factory for the Chrome driver.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from cookie_clicker_bot.constants import ELEMENT_TIMEOUT_SECONDS

_HEADLESS_ARGUMENTS: tuple[str, ...] = (
    "--headless=new",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--window-size=1280,1024",
)


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
        WebDriverWait(self._driver, ELEMENT_TIMEOUT_SECONDS).until(
            expected_conditions.presence_of_element_located((By.ID, element_id))
        )

    def click_element(self, element_id: str) -> None:
        """@brief Click the element with a real click, never a script click.

        The game rate-limits synthetic clicks, so the click must come from the
        browser the way a user's does.

        @param element_id The HTML id of the element.
        @throws selenium.common.exceptions.TimeoutException When it never
            becomes clickable.
        """
        element = WebDriverWait(self._driver, ELEMENT_TIMEOUT_SECONDS).until(
            expected_conditions.element_to_be_clickable((By.ID, element_id))
        )
        element.click()

    def read_text(self, element_id: str) -> str:
        """@brief Return the visible text of the element.
        @param element_id The HTML id of the element.
        @return The text as shown on the page.
        """
        return self._driver.find_element(By.ID, element_id).text

    def read_attribute(self, element_id: str, attribute: str) -> str:
        """@brief Return an attribute of the element.
        @param element_id The HTML id of the element.
        @param attribute The attribute name, for example "class".
        @return The value, or an empty string when the attribute is absent.
        """
        value = self._driver.find_element(By.ID, element_id).get_attribute(attribute)
        return value or ""

    def close(self) -> None:
        """@brief Quit the browser and end the driver session."""
        self._driver.quit()


def create_chrome_driver(headless: bool = False) -> WebDriver:
    """@brief Build a Chrome web driver.
    @param headless True to run without a window, for a container or CI.
    @return The started Chrome driver.
    """
    options = webdriver.ChromeOptions()
    if headless:
        for argument in _HEADLESS_ARGUMENTS:
            options.add_argument(argument)
    return webdriver.Chrome(options=options)
