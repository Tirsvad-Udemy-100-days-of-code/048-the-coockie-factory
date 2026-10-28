"""@file
@brief Lecture step 5: play for a set time, buying upgrades, then report the rate.
"""

import logging
from decimal import Decimal

from cookie_clicker_bot.application.ports.clock import Clock
from cookie_clicker_bot.application.ports.game_port import GamePort
from cookie_clicker_bot.application.use_cases.bot_core import click_cookie
from cookie_clicker_bot.application.use_cases.store import (
    buy_available_upgrades,
    buy_upgrade,
    get_cps,
    get_store_items,
)
from cookie_clicker_bot.constants import (
    CLICKS_PER_BURST,
    RUN_DURATION_SECONDS,
    STORE_CHECK_INTERVAL_SECONDS,
)
from cookie_clicker_bot.domain.store_item import choose_upgrade

_logger = logging.getLogger(__name__)


def _buy_best_product(game: GamePort) -> bool:
    """@brief Buy the best affordable product, at most one, from a fresh read.

    The game updates the owned amount at once but the affordable flags only at
    its next draw, so a second purchase in the same visit would read stale flags.
    """
    item = choose_upgrade(get_store_items(game))
    if item is None:
        return False
    if not buy_upgrade(game, item):
        _logger.warning(
            "Purchase of product %d did not raise the owned amount", item.index
        )
        return False
    _logger.info("Bought product %d for %d cookies", item.index, item.price)
    return True


def run_bot(
    game: GamePort,
    clock: Clock,
    duration_seconds: float = RUN_DURATION_SECONDS,
) -> Decimal:
    """@brief Click the cookie and buy upgrades until the time is up.

    One loop: a burst of clicks, then, every store check interval, a visit to
    the store that buys the affordable upgrades, cheapest first, and then at
    most one product, the most expensive affordable one.

    @param game The game page to operate.
    @param clock The clock that measures the run.
    @param duration_seconds How long to play, more than zero.
    @return The cookies per second at the end of the run.
    @throws ValueError When duration_seconds is zero or negative.
    """
    if duration_seconds <= 0:
        raise ValueError(f"duration_seconds must be positive, got {duration_seconds}")
    start = clock.monotonic()
    next_store_check = start + STORE_CHECK_INTERVAL_SECONDS
    now = start
    while now - start < duration_seconds:
        click_cookie(game, CLICKS_PER_BURST)
        now = clock.monotonic()
        if now >= next_store_check:
            buy_available_upgrades(game)
            _buy_best_product(game)
            next_store_check = now + STORE_CHECK_INTERVAL_SECONDS
            _logger.info("%.0f of %s seconds played", now - start, duration_seconds)
    cps = get_cps(game)
    _logger.info("Run finished at %s cookies per second", cps)
    return cps
