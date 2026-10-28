"""@file
@brief Tests of the Selenium adapter against a hand-written fake driver.

No browser and no network: the fake driver records what the adapter asks for.
"""

from typing import cast

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from cookie_clicker_bot.infrastructure.selenium_game import SeleniumGame


class FakeElement:
    """@brief An element that counts its real clicks."""

    def __init__(self, text: str = "") -> None:
        self.text = text
        self.clicks = 0

    def is_displayed(self) -> bool:
        return True

    def is_enabled(self) -> bool:
        return True

    def click(self) -> None:
        self.clicks += 1


class FakeDriver:
    """@brief A driver with elements by id; it records its calls."""

    def __init__(self, elements: dict[str, FakeElement]) -> None:
        self.elements = elements
        self.visited: list[str] = []
        self.lookups: list[tuple[str, str]] = []
        self.quit_calls = 0

    def get(self, url: str) -> None:
        self.visited.append(url)

    def find_element(self, by: str, value: str) -> FakeElement:
        self.lookups.append((by, value))
        if value not in self.elements:
            raise NoSuchElementException(value)
        return self.elements[value]

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


def test_close_quits_the_driver() -> None:
    driver = FakeDriver({})

    make_game(driver).close()

    assert driver.quit_calls == 1
