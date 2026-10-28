"""@file
@brief Tests of get_store_items, buy_upgrade and get_cps against a fake game.
"""

from decimal import Decimal

import pytest

from cookie_clicker_bot.application.use_cases.store import (
    buy_upgrade,
    get_cps,
    get_store_items,
)
from cookie_clicker_bot.constants import (
    CLASS_ATTRIBUTE,
    COOKIE_COUNTER_ID,
    CPS_ID,
    PRODUCT_ID_PREFIX,
    PRODUCT_PRICE_ID_PREFIX,
)
from cookie_clicker_bot.domain.errors import UnreadableNumberError
from cookie_clicker_bot.domain.store_item import StoreItem
from tests.unit.fakes import FakeGame


def make_store(classes: dict[int, str], prices: dict[int, str]) -> FakeGame:
    attributes = {
        (f"{PRODUCT_ID_PREFIX}{i}", CLASS_ATTRIBUTE): c for i, c in classes.items()
    }
    texts = {f"{PRODUCT_PRICE_ID_PREFIX}{i}": p for i, p in prices.items()}
    return FakeGame(texts=texts, attributes=attributes)


def test_get_store_items_skips_locked_products() -> None:
    game = make_store(
        {0: "product unlocked enabled", 1: "product locked disabled", 2: "product"},
        {0: "15", 1: "100", 2: "1,100"},
    )
    assert get_store_items(game) == [StoreItem(0, 15, True)]


def test_get_store_items_reads_price_and_affordability() -> None:
    game = make_store(
        {
            0: "product unlocked enabled",
            1: "product unlocked disabled",
            2: "product unlocked disabled",
        },
        {0: "15", 1: "1,100", 2: "1.5 million"},
    )
    assert get_store_items(game) == [
        StoreItem(0, 15, True),
        StoreItem(1, 1100, False),
        StoreItem(2, 1_500_000, False),
    ]


def test_get_store_items_is_empty_when_nothing_is_unlocked() -> None:
    assert get_store_items(FakeGame()) == []


def test_get_store_items_propagates_an_unreadable_price() -> None:
    game = make_store({0: "product unlocked"}, {0: "???"})
    with pytest.raises(UnreadableNumberError):
        get_store_items(game)


def test_buy_upgrade_returns_true_when_the_cookies_drop() -> None:
    game = FakeGame(texts={COOKIE_COUNTER_ID: "100 cookies"})

    def spend(element_id: str) -> None:
        game.texts[COOKIE_COUNTER_ID] = "85 cookies"

    game.on_click = spend
    assert buy_upgrade(game, StoreItem(3, 15, True)) is True
    assert game.clicked == [f"{PRODUCT_ID_PREFIX}3"]


def test_buy_upgrade_returns_false_when_the_cookies_do_not_drop() -> None:
    game = FakeGame(texts={COOKIE_COUNTER_ID: "100 cookies"})
    assert buy_upgrade(game, StoreItem(3, 15, True)) is False
    assert game.clicked == [f"{PRODUCT_ID_PREFIX}3"]


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("per second: 0.1", Decimal("0.1")),
        ("per second: 1,234.5", Decimal("1234.5")),
        ("per second: 1.234 million", Decimal("1234000")),
        ("per second: 0", Decimal(0)),
    ],
)
def test_get_cps_reads_the_amount_after_the_colon(text: str, expected: Decimal) -> None:
    assert get_cps(FakeGame(texts={CPS_ID: text})) == expected


def test_get_cps_rejects_a_line_without_amount() -> None:
    with pytest.raises(UnreadableNumberError):
        get_cps(FakeGame(texts={CPS_ID: "per second"}))
