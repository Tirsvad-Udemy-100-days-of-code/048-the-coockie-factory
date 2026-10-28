"""@file
@brief Tests of the run loop against a fake game and a fake clock.
"""

from decimal import Decimal

import pytest

from cookie_clicker_bot.application.use_cases.run_bot import run_bot
from cookie_clicker_bot.constants import (
    BIG_COOKIE_ID,
    CLASS_ATTRIBUTE,
    CLICKS_PER_BURST,
    COOKIE_COUNTER_ID,
    CPS_ID,
    FIRST_UPGRADE_ID,
    PRODUCT_ID_PREFIX,
    PRODUCT_OWNED_ID_PREFIX,
    PRODUCT_PRICE_ID_PREFIX,
    RUN_DURATION_SECONDS,
    STORE_CHECK_INTERVAL_SECONDS,
    UPGRADE_IDENTITY_ATTRIBUTE,
)
from cookie_clicker_bot.domain.errors import UnreadableNumberError
from tests.unit.fakes import FakeClock, FakeGame

PRODUCT = f"{PRODUCT_ID_PREFIX}0"


def make_game(cookies: int = 100, price: int = 15) -> FakeGame:
    """A store with one affordable product that is spent once, then unaffordable."""
    game = FakeGame(
        texts={
            COOKIE_COUNTER_ID: f"{cookies} cookies",
            f"{PRODUCT_PRICE_ID_PREFIX}0": str(price),
            CPS_ID: "per second: 4.5",
            f"{PRODUCT_OWNED_ID_PREFIX}0": "",
        },
        attributes={(PRODUCT, CLASS_ATTRIBUTE): "product unlocked enabled"},
    )

    def spend(element_id: str) -> None:
        if element_id == PRODUCT:
            game.texts[COOKIE_COUNTER_ID] = f"{cookies - price} cookies"
            game.texts[f"{PRODUCT_OWNED_ID_PREFIX}0"] = "1"
            game.attributes[(PRODUCT, CLASS_ATTRIBUTE)] = "product unlocked disabled"

    game.on_click = spend
    return game


def test_run_bot_returns_the_cps() -> None:
    assert run_bot(make_game(), FakeClock(), 3) == Decimal("4.5")


def test_run_bot_clicks_in_bursts_until_the_duration_is_over() -> None:
    game = FakeGame(texts={CPS_ID: "per second: 1"})
    run_bot(game, FakeClock(step=1.0), 3)
    assert game.clicked == [BIG_COOKIE_ID] * CLICKS_PER_BURST * 3


def test_run_bot_stops_after_the_duration() -> None:
    clock = FakeClock(step=10.0)
    game = FakeGame(texts={CPS_ID: "per second: 1"})
    run_bot(game, clock, 25)
    assert clock.now == 40.0


def test_run_bot_does_not_visit_the_store_before_the_interval() -> None:
    game = make_game()
    run_bot(game, FakeClock(step=0.25), STORE_CHECK_INTERVAL_SECONDS * 0.75)
    assert PRODUCT not in game.clicked


def test_run_bot_buys_at_the_interval() -> None:
    game = make_game()
    run_bot(game, FakeClock(step=1.0), STORE_CHECK_INTERVAL_SECONDS + 2)
    assert game.clicked.count(PRODUCT) == 1


def test_run_bot_buys_crates_before_products() -> None:
    game = make_game()
    game.attributes[(FIRST_UPGRADE_ID, CLASS_ATTRIBUTE)] = "crate upgrade enabled"
    game.attributes[(FIRST_UPGRADE_ID, UPGRADE_IDENTITY_ATTRIBUTE)] = "7"
    previous = game.on_click

    def click(element_id: str) -> None:
        if element_id == FIRST_UPGRADE_ID:
            game.attributes[(FIRST_UPGRADE_ID, UPGRADE_IDENTITY_ATTRIBUTE)] = "8"
            game.attributes[(FIRST_UPGRADE_ID, CLASS_ATTRIBUTE)] = "crate disabled"
        elif previous is not None:
            previous(element_id)

    game.on_click = click
    run_bot(game, FakeClock(step=1.0), STORE_CHECK_INTERVAL_SECONDS)
    assert [c for c in game.clicked if c in (FIRST_UPGRADE_ID, PRODUCT)] == [
        FIRST_UPGRADE_ID,
        PRODUCT,
    ]


def test_run_bot_buys_one_product_per_visit_and_the_next_at_the_next_visit(
    caplog: pytest.LogCaptureFixture,
) -> None:
    game = FakeGame(
        texts={
            CPS_ID: "per second: 1",
            f"{PRODUCT_PRICE_ID_PREFIX}0": "15",
            f"{PRODUCT_PRICE_ID_PREFIX}1": "50",
            f"{PRODUCT_OWNED_ID_PREFIX}0": "",
            f"{PRODUCT_OWNED_ID_PREFIX}1": "",
        },
        attributes={
            (f"{PRODUCT_ID_PREFIX}0", CLASS_ATTRIBUTE): "product unlocked enabled",
            (f"{PRODUCT_ID_PREFIX}1", CLASS_ATTRIBUTE): "product unlocked enabled",
        },
    )
    visits: list[int] = []

    def click(element_id: str) -> None:
        if element_id.startswith(PRODUCT_ID_PREFIX):
            index = element_id.removeprefix(PRODUCT_ID_PREFIX)
            visits.append(int(index))
            game.texts[f"{PRODUCT_OWNED_ID_PREFIX}{index}"] = "1"
            game.attributes[(element_id, CLASS_ATTRIBUTE)] = "product unlocked"

    game.on_click = click
    with caplog.at_level("WARNING"):
        run_bot(game, FakeClock(step=1.0), STORE_CHECK_INTERVAL_SECONDS * 2)
    assert visits == [1, 0]
    assert caplog.records == []


def test_run_bot_buys_nothing_more_when_nothing_is_affordable() -> None:
    game = make_game()
    run_bot(game, FakeClock(step=1.0), STORE_CHECK_INTERVAL_SECONDS * 3)
    assert game.clicked.count(PRODUCT) == 1


def test_run_bot_stops_buying_when_a_purchase_fails() -> None:
    game = make_game()
    game.on_click = None
    run_bot(game, FakeClock(step=1.0), STORE_CHECK_INTERVAL_SECONDS)
    assert game.clicked.count(PRODUCT) == 1


@pytest.mark.parametrize("duration", [0, -1])
def test_run_bot_rejects_a_non_positive_duration(duration: float) -> None:
    game = FakeGame()
    with pytest.raises(ValueError, match="positive"):
        run_bot(game, FakeClock(), duration)
    assert game.clicked == []


def test_run_bot_propagates_an_unreadable_cps() -> None:
    game = FakeGame(texts={CPS_ID: "nothing"})
    with pytest.raises(UnreadableNumberError):
        run_bot(game, FakeClock(), 1)


def test_run_duration_default_is_the_constant() -> None:
    clock = FakeClock(step=100.0)
    game = FakeGame(texts={CPS_ID: "per second: 1"})
    run_bot(game, clock)
    assert clock.now == 100.0 * (RUN_DURATION_SECONDS // 100 + 1)
