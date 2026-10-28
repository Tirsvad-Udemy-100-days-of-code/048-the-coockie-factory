"""@file
@brief Lecture step 4: read the store, buy a product and read the cookies per second.
"""

from decimal import Decimal

from cookie_clicker_bot.application.ports.game_port import GamePort
from cookie_clicker_bot.application.use_cases.bot_core import get_cookie_count
from cookie_clicker_bot.constants import (
    CLASS_ATTRIBUTE,
    CPS_ID,
    CPS_SEPARATOR,
    ENABLED_CLASS,
    PRODUCT_COUNT,
    PRODUCT_ID_PREFIX,
    PRODUCT_PRICE_ID_PREFIX,
    UNLOCKED_CLASS,
)
from cookie_clicker_bot.domain.number_parsing import (
    parse_game_decimal,
    parse_game_number,
)
from cookie_clicker_bot.domain.store_item import StoreItem


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


def buy_upgrade(game: GamePort, item: StoreItem) -> bool:
    """@brief Click a product and check that the purchase went through.
    @param game The game page to operate.
    @param item The product to buy.
    @return True when the cookie count dropped after the click.
    """
    before = get_cookie_count(game)
    game.click_element(PRODUCT_ID_PREFIX + str(item.index))
    return get_cookie_count(game) < before


def get_cps(game: GamePort) -> Decimal:
    """@brief Read the cookies per second the bakery makes now.
    @param game The game page to read.
    @return The rate, with its decimals.
    @throws UnreadableNumberError When the line shows no number.
    """
    text = game.read_text(CPS_ID)
    return parse_game_decimal(text.partition(CPS_SEPARATOR)[2])
