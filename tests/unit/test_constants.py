"""@file
@brief Guards the timing constants the bot relies on.
"""

from cookie_clicker_bot import constants


def test_run_duration_is_five_minutes() -> None:
    assert constants.RUN_DURATION_SECONDS == 300


def test_store_is_visited_every_second() -> None:
    assert constants.STORE_CHECK_INTERVAL_SECONDS == 1


def test_store_check_happens_inside_the_run() -> None:
    assert 0 < constants.STORE_CHECK_INTERVAL_SECONDS < constants.RUN_DURATION_SECONDS
