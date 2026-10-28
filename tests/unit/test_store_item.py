"""@file
@brief Tests of the purchase strategy choose_upgrade.
"""

import dataclasses

import pytest

from cookie_clicker_bot.domain.store_item import StoreItem, choose_upgrade


def test_choose_upgrade_picks_the_most_expensive_affordable_item() -> None:
    items = [StoreItem(0, 15, True), StoreItem(1, 100, True), StoreItem(2, 1100, False)]
    assert choose_upgrade(items) == StoreItem(1, 100, True)


def test_choose_upgrade_returns_none_when_nothing_is_affordable() -> None:
    assert choose_upgrade([StoreItem(0, 15, False), StoreItem(1, 100, False)]) is None


def test_choose_upgrade_returns_none_for_an_empty_store() -> None:
    assert choose_upgrade([]) is None


def test_choose_upgrade_returns_the_only_item_when_it_is_affordable() -> None:
    item = StoreItem(0, 15, True)
    assert choose_upgrade([item]) == item


def test_choose_upgrade_prefers_the_highest_index_on_equal_price() -> None:
    items = [StoreItem(3, 50, True), StoreItem(7, 50, True), StoreItem(5, 50, True)]
    assert choose_upgrade(items) == StoreItem(7, 50, True)


def test_choose_upgrade_trusts_the_affordable_flag_at_price_boundary() -> None:
    items = [StoreItem(0, 15, True), StoreItem(1, 16, False)]
    assert choose_upgrade(items) == StoreItem(0, 15, True)


def test_choose_upgrade_ignores_the_order_of_the_items() -> None:
    items = [StoreItem(2, 500, True), StoreItem(0, 15, True), StoreItem(1, 100, True)]
    assert choose_upgrade(items) == StoreItem(2, 500, True)


def test_store_item_is_immutable() -> None:
    item = StoreItem(0, 15, True)
    with pytest.raises(dataclasses.FrozenInstanceError):
        item.price = 1  # type: ignore[misc]
