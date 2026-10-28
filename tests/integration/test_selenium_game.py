"""@file
@brief Tests of the Selenium adapter against a hand-written fake driver.

No browser and no network: the fake driver records what the adapter asks for.
"""

from pathlib import Path
from typing import cast

import pytest
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from cookie_clicker_bot.constants import CHROME_BIN_ENV, CHROMEDRIVER_ENV, CLICK_RETRIES
from cookie_clicker_bot.infrastructure.selenium_game import (
    SeleniumGame,
    build_chrome_options,
    build_chrome_service,
)


class FakeElement:
    """@brief An element that counts its real clicks."""

    def __init__(
        self, text: str = "", attributes: dict[str, str | None] | None = None
    ) -> None:
        self.text = text
        self.attributes = attributes or {}
        self.clicks = 0
        self.failures: list[Exception] = []

    def get_attribute(self, name: str) -> str | None:
        return self.attributes.get(name)

    def is_displayed(self) -> bool:
        return True

    def is_enabled(self) -> bool:
        return True

    def click(self) -> None:
        if self.failures:
            raise self.failures.pop(0)
        self.clicks += 1


class FakeDriver:
    """@brief A driver with elements by id; it records its calls."""

    def __init__(self, elements: dict[str, FakeElement]) -> None:
        self.elements = elements
        self.visited: list[str] = []
        self.lookups: list[tuple[str, str]] = []
        self.quit_calls = 0
        self.screenshots: list[str] = []
        self.lookup_failures: list[Exception] = []

    def get(self, url: str) -> None:
        self.visited.append(url)

    def find_element(self, by: str, value: str) -> FakeElement:
        self.lookups.append((by, value))
        if self.lookup_failures:
            raise self.lookup_failures.pop(0)
        if value not in self.elements:
            raise NoSuchElementException(value)
        return self.elements[value]

    def save_screenshot(self, filename: str) -> bool:
        self.screenshots.append(filename)
        return True

    def quit(self) -> None:
        self.quit_calls += 1


def make_game(driver: FakeDriver) -> SeleniumGame:
    return SeleniumGame(cast(WebDriver, driver))


def test_open_page_loads_the_url() -> None:
    driver = FakeDriver({})

    make_game(driver).open_page("https://example.test/")

    assert driver.visited == ["https://example.test/"]


def test_wait_for_element_looks_up_by_id() -> None:
    driver = FakeDriver({"bigCookie": FakeElement()})

    make_game(driver).wait_for_element("bigCookie")

    assert driver.lookups == [(By.ID, "bigCookie")]


def test_read_text_returns_the_element_text() -> None:
    driver = FakeDriver({"cookies": FakeElement("12 cookies")})

    assert make_game(driver).read_text("cookies") == "12 cookies"
    assert driver.lookups == [(By.ID, "cookies")]


def test_click_element_makes_one_real_click() -> None:
    element = FakeElement()
    driver = FakeDriver({"bigCookie": element})

    make_game(driver).click_element("bigCookie")

    assert element.clicks == 1
    assert all(by == By.ID for by, _ in driver.lookups)


def test_read_text_raises_when_element_is_missing() -> None:
    game = make_game(FakeDriver({}))

    with pytest.raises(NoSuchElementException):
        game.read_text("missing")


def test_read_attribute_returns_the_attribute_value() -> None:
    driver = FakeDriver(
        {"product0": FakeElement(attributes={"class": "product unlocked"})}
    )

    assert make_game(driver).read_attribute("product0", "class") == "product unlocked"
    assert driver.lookups == [(By.ID, "product0")]


def test_read_attribute_returns_empty_string_when_absent() -> None:
    driver = FakeDriver({"product0": FakeElement()})

    assert make_game(driver).read_attribute("product0", "class") == ""


def test_click_element_retries_after_a_stale_element() -> None:
    element = FakeElement()
    element.failures = [StaleElementReferenceException()] * CLICK_RETRIES
    driver = FakeDriver({"bigCookie": element})

    make_game(driver).click_element("bigCookie")

    assert element.clicks == 1
    assert len(driver.lookups) == CLICK_RETRIES + 1


def test_click_element_retries_after_an_intercepted_click() -> None:
    element = FakeElement()
    element.failures = [ElementClickInterceptedException()]

    make_game(FakeDriver({"bigCookie": element})).click_element("bigCookie")

    assert element.clicks == 1


def test_click_element_raises_after_the_retry_limit() -> None:
    element = FakeElement()
    element.failures = [StaleElementReferenceException()] * (CLICK_RETRIES + 1)
    driver = FakeDriver({"bigCookie": element})

    with pytest.raises(StaleElementReferenceException):
        make_game(driver).click_element("bigCookie")

    assert element.clicks == 0
    assert len(driver.lookups) == CLICK_RETRIES + 1


def test_read_text_retries_after_a_stale_element() -> None:
    driver = FakeDriver({"cookies": FakeElement("5")})
    driver.lookup_failures = [StaleElementReferenceException()] * CLICK_RETRIES

    assert make_game(driver).read_text("cookies") == "5"


def test_read_attribute_raises_after_the_retry_limit() -> None:
    driver = FakeDriver({"product0": FakeElement()})
    driver.lookup_failures = [StaleElementReferenceException()] * (CLICK_RETRIES + 1)

    with pytest.raises(StaleElementReferenceException):
        make_game(driver).read_attribute("product0", "class")


def test_save_screenshot_creates_the_folder_and_writes_the_file(
    tmp_path: Path,
) -> None:
    driver = FakeDriver({})
    target = tmp_path / "nested" / "shot.png"

    make_game(driver).save_screenshot(target)

    assert driver.screenshots == [str(target)]
    assert target.parent.is_dir()


def test_chrome_options_use_the_binary_from_the_environment() -> None:
    options = build_chrome_options(True, {CHROME_BIN_ENV: "/usr/bin/chromium"})

    assert options.binary_location == "/usr/bin/chromium"
    assert "--headless=new" in options.arguments
    assert "--no-sandbox" in options.arguments


def test_chrome_options_leave_the_binary_alone_without_the_variable() -> None:
    options = build_chrome_options(False, {})

    assert options.binary_location == ""
    assert options.arguments == []


def test_chrome_service_uses_the_driver_from_the_environment() -> None:
    service = build_chrome_service({CHROMEDRIVER_ENV: "/usr/bin/chromedriver"})

    assert service is not None
    assert service.path == "/usr/bin/chromedriver"


def test_chrome_service_is_absent_without_the_variable() -> None:
    assert build_chrome_service({}) is None


def test_close_quits_the_driver() -> None:
    driver = FakeDriver({})

    make_game(driver).close()

    assert driver.quit_calls == 1
