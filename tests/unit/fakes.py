"""@file
@brief A fake game page for tests that must not start a browser.
"""


class FakeGame:
    """@brief Records what the bot does and answers reads from a dictionary."""

    def __init__(self, texts: dict[str, str] | None = None) -> None:
        self.texts: dict[str, str] = texts or {}
        self.opened: list[str] = []
        self.waited: list[str] = []
        self.clicked: list[str] = []

    def open_page(self, url: str) -> None:
        self.opened.append(url)

    def wait_for_element(self, element_id: str) -> None:
        self.waited.append(element_id)

    def click_element(self, element_id: str) -> None:
        self.clicked.append(element_id)

    def read_text(self, element_id: str) -> str:
        return self.texts[element_id]
