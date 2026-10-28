"""@file
@brief Fakes of the ports for tests that must not start a browser or sleep.
"""

from collections.abc import Callable


class FakeGame:
    """@brief Records what the bot does and answers reads from dictionaries."""

    def __init__(
        self,
        texts: dict[str, str] | None = None,
        attributes: dict[tuple[str, str], str] | None = None,
        on_click: Callable[[str], None] | None = None,
        text_sequences: dict[str, list[str]] | None = None,
    ) -> None:
        self.texts: dict[str, str] = texts or {}
        self.attributes: dict[tuple[str, str], str] = attributes or {}
        self.on_click = on_click
        ## Texts returned one per read, before the plain text applies.
        self.text_sequences: dict[str, list[str]] = text_sequences or {}
        self.reads: dict[str, int] = {}
        self.opened: list[str] = []
        self.waited: list[str] = []
        self.clicked: list[str] = []
        self.close_calls = 0

    def open_page(self, url: str) -> None:
        self.opened.append(url)

    def wait_for_element(self, element_id: str) -> None:
        self.waited.append(element_id)

    def click_element(self, element_id: str) -> None:
        self.clicked.append(element_id)
        if self.on_click is not None:
            self.on_click(element_id)

    def read_text(self, element_id: str) -> str:
        self.reads[element_id] = self.reads.get(element_id, 0) + 1
        queued = self.text_sequences.get(element_id)
        if queued:
            return queued.pop(0)
        return self.texts[element_id]

    def read_attribute(self, element_id: str, attribute: str) -> str:
        return self.attributes.get((element_id, attribute), "")

    def close(self) -> None:
        self.close_calls += 1


class FakeClock:
    """@brief A clock that moves forward by a fixed step on every reading."""

    def __init__(self, step: float = 1.0) -> None:
        self.now = 0.0
        self.step = step

    def monotonic(self) -> float:
        reading = self.now
        self.now += self.step
        return reading
