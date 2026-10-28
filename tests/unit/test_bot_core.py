"""@file
@brief Tests of lecture steps 1 to 3 against a fake game.
"""

import pytest

from cookie_clicker_bot.application.use_cases.bot_core import (
    click_cookie,
    get_cookie_count,
    open_game,
    select_language,
)
from cookie_clicker_bot.constants import (
    BIG_COOKIE_ID,
    COOKIE_COUNTER_ID,
    GAME_URL,
    LANGUAGE_BUTTON_PREFIX,
    LANGUAGE_CODE,
)
from tests.unit.fakes import FakeGame

LANGUAGE_BUTTON = LANGUAGE_BUTTON_PREFIX + LANGUAGE_CODE


def test_open_game_loads_the_url_and_waits_for_the_language_prompt() -> None:
    game = FakeGame()
    open_game(game)
    assert game.opened == [GAME_URL]
    assert game.waited == [LANGUAGE_BUTTON]


def test_select_language_clicks_the_button_and_waits_for_the_cookie() -> None:
    game = FakeGame()
    select_language(game)
    assert game.clicked == [LANGUAGE_BUTTON]
    assert game.waited == [BIG_COOKIE_ID]


@pytest.mark.parametrize("times", [0, 1, 2, 50])
def test_click_cookie_clicks_the_requested_number_of_times(times: int) -> None:
    game = FakeGame()
    click_cookie(game, times)
    assert game.clicked == [BIG_COOKIE_ID] * times


def test_click_cookie_defaults_to_one_click() -> None:
    game = FakeGame()
    click_cookie(game)
    assert game.clicked == [BIG_COOKIE_ID]


def test_click_cookie_refuses_a_negative_count() -> None:
    game = FakeGame()
    with pytest.raises(ValueError, match="negative"):
        click_cookie(game, -1)
    assert game.clicked == []


def test_get_cookie_count_reads_the_first_line_of_the_counter() -> None:
    game = FakeGame({COOKIE_COUNTER_ID: "12,345 cookies\nper second: 3.5"})
    assert get_cookie_count(game) == 12345


def test_get_cookie_count_reads_large_amounts_split_over_lines() -> None:
    game = FakeGame({COOKIE_COUNTER_ID: "1.234 million\ncookies\nper second: 900"})
    assert get_cookie_count(game) == 1_234_000
