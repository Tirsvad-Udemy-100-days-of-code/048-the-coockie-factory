"""@file
@brief Lecture steps 1 to 3: open the game, click the cookie, read the count.
"""

from cookie_clicker_bot.application.ports.game_port import GamePort
from cookie_clicker_bot.constants import (
    BIG_COOKIE_ID,
    COOKIE_COUNTER_ID,
    GAME_URL,
    LANGUAGE_BUTTON_PREFIX,
    LANGUAGE_CODE,
)
from cookie_clicker_bot.domain.number_parsing import parse_game_number


def open_game(game: GamePort) -> None:
    """@brief Load the game and wait until it asks for a language.
    @param game The game page to operate.
    """
    game.open_page(GAME_URL)
    game.wait_for_element(LANGUAGE_BUTTON_PREFIX + LANGUAGE_CODE)


def select_language(game: GamePort) -> None:
    """@brief Choose the language and wait until the big cookie is playable.
    @param game The game page to operate.
    """
    game.click_element(LANGUAGE_BUTTON_PREFIX + LANGUAGE_CODE)
    game.wait_for_element(BIG_COOKIE_ID)


def click_cookie(game: GamePort, times: int = 1) -> None:
    """@brief Click the big cookie.
    @param game The game page to operate.
    @param times How many clicks to make, zero or more.
    @throws ValueError When times is negative.
    """
    if times < 0:
        raise ValueError(f"times must not be negative, got {times}")
    for _ in range(times):
        game.click_element(BIG_COOKIE_ID)


def get_cookie_count(game: GamePort) -> int:
    """@brief Read how many cookies the bakery has now.
    @param game The game page to read.
    @return The number of cookies, rounded to a whole number.
    @throws UnreadableNumberError When the counter shows no number.
    """
    first_line = game.read_text(COOKIE_COUNTER_ID).strip().splitlines()[0]
    return parse_game_number(first_line)
