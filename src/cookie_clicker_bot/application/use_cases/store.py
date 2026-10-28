"""@file
@brief Lecture step 4: read the store, buy a product and read the cookies per second.
"""

import logging
from decimal import Decimal

from cookie_clicker_bot.application.ports.game_port import GamePort
from cookie_clicker_bot.constants import (
    CLASS_ATTRIBUTE,
    CPS_ID,
    CPS_SEPARATOR,
    ENABLED_CLASS,
    FIRST_UPGRADE_ID,
    OWNED_CHECK_ATTEMPTS,
    PRODUCT_COUNT,
    PRODUCT_ID_PREFIX,
    PRODUCT_OWNED_ID_PREFIX,
    PRODUCT_PRICE_ID_PREFIX,
    REDRAW_CHECK_ATTEMPTS,
    UNLOCKED_CLASS,
    UPGRADE_BUY_LIMIT,
    UPGRADE_IDENTITY_ATTRIBUTE,
)
from cookie_clicker_bot.domain.number_parsing import (
    parse_game_decimal,
    parse_game_number,
)
from cookie_clicker_bot.domain.store_item import StoreItem

_logger = logging.getLogger(__name__)


def get_store_items(game: GamePort) -> list[StoreItem]:
    """@brief Read the products that are visible in the store.
    @param game The game page to read.
    @return One item per unlocked product, in store order.
    @throws UnreadableNumberError When a price shows no number.
    """
    items: list[StoreItem] = []
    for index in range(PRODUCT_COUNT):
        classes = game.read_attribute(
            PRODUCT_ID_PREFIX + str(index), CLASS_ATTRIBUTE
        ).split()
        if UNLOCKED_CLASS not in classes:
            continue
        price = parse_game_number(game.read_text(PRODUCT_PRICE_ID_PREFIX + str(index)))
        items.append(StoreItem(index, price, ENABLED_CLASS in classes))
    return items


def _read_owned(game: GamePort, index: int) -> int:
    """@brief Read how many of a product is owned; the game shows none as empty."""
    text = game.read_text(PRODUCT_OWNED_ID_PREFIX + str(index)).strip()
    return parse_game_number(text) if text else 0


def buy_upgrade(game: GamePort, item: StoreItem) -> bool:
    """@brief Click a product and check that the purchase went through.

    The game redraws the page a moment after the click, so the owned amount is
    read again, up to OWNED_CHECK_ATTEMPTS times, until it has grown.

    @param game The game page to operate.
    @param item The product to buy.
    @return True when the owned amount of the product grew after the click.
    @throws UnreadableNumberError When the owned amount shows no number.
    """
    before = _read_owned(game, item.index)
    game.click_element(PRODUCT_ID_PREFIX + str(item.index))
    return any(
        _read_owned(game, item.index) > before for _ in range(OWNED_CHECK_ATTEMPTS)
    )


def _first_upgrade_is_affordable(game: GamePort) -> bool:
    if not game.has_element(FIRST_UPGRADE_ID):
        return False
    return (
        ENABLED_CLASS in game.read_attribute(FIRST_UPGRADE_ID, CLASS_ATTRIBUTE).split()
    )


def _upgrade_was_replaced(game: GamePort, old_identity: str) -> bool:
    """@brief Wait until the first crate shows another upgrade or is gone."""
    for _ in range(REDRAW_CHECK_ATTEMPTS):
        if not game.has_element(FIRST_UPGRADE_ID):
            return True
        identity = game.read_attribute(FIRST_UPGRADE_ID, UPGRADE_IDENTITY_ATTRIBUTE)
        if identity != old_identity:
            return True
    return False


def buy_available_upgrades(game: GamePort) -> int:
    """@brief Buy the upgrade crates the player can afford, cheapest first.

    The crates are numbered by price and numbered again after each purchase, so
    the cheapest one is always the first. The loop stops at the first crate that
    is missing or unaffordable, at UPGRADE_BUY_LIMIT, or when a click leaves the
    crate unchanged.

    @param game The game page to operate.
    @return How many upgrades were bought.
    """
    bought = 0
    while bought < UPGRADE_BUY_LIMIT and _first_upgrade_is_affordable(game):
        identity = game.read_attribute(FIRST_UPGRADE_ID, UPGRADE_IDENTITY_ATTRIBUTE)
        game.click_element(FIRST_UPGRADE_ID)
        if not _upgrade_was_replaced(game, identity):
            _logger.warning("Upgrade %s stayed in the store after the click", identity)
            break
        bought += 1
        _logger.info("Bought upgrade %s", identity)
    return bought


def get_cps(game: GamePort) -> Decimal:
    """@brief Read the cookies per second the bakery makes now.
    @param game The game page to read.
    @return The rate, with its decimals.
    @throws UnreadableNumberError When the line shows no number.
    """
    text = game.read_text(CPS_ID)
    return parse_game_decimal(text.partition(CPS_SEPARATOR)[2])
