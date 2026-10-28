"""@file
@brief A product in the store and the rule that picks which one to buy.
"""

from collections.abc import Sequence
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class StoreItem:
    """@brief A product that is visible in the store.

    @param index Position of the product in the store, from zero.
    @param price Cookies the product costs now.
    @param is_affordable True when the player has enough cookies to buy it.
    """

    index: int
    price: int
    is_affordable: bool


def choose_upgrade(items: Sequence[StoreItem]) -> StoreItem | None:
    """@brief Pick the most expensive product the player can afford.

    A tie in price goes to the product with the highest index.

    @param items The visible products.
    @return The product to buy, or None when nothing is affordable.
    """
    affordable = [item for item in items if item.is_affordable]
    if not affordable:
        return None
    return max(affordable, key=lambda item: (item.price, item.index))
