"""@file
@brief The port through which the bot sees and operates the game.
"""

from typing import Protocol


class GamePort(Protocol):
    """@brief A running game page. The Selenium adapter implements it."""

    def open_page(self, url: str) -> None:
        """@brief Load the page at the address.
        @param url The address of the game.
        """
        ...

    def wait_for_element(self, element_id: str) -> None:
        """@brief Block until the element is on the page.
        @param element_id The HTML id of the element.
        """
        ...

    def click_element(self, element_id: str) -> None:
        """@brief Click the element the way a user does.
        @param element_id The HTML id of the element.
        """
        ...

    def read_text(self, element_id: str) -> str:
        """@brief Return the visible text of the element.
        @param element_id The HTML id of the element.
        @return The text as shown on the page.
        """
        ...

    def read_attribute(self, element_id: str, attribute: str) -> str:
        """@brief Return an attribute of the element.
        @param element_id The HTML id of the element.
        @param attribute The attribute name, for example "class".
        @return The value, or an empty string when the attribute is absent.
        """
        ...
