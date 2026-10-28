"""@file
@brief Entry point that plays the five lecture steps and saves a screenshot after each.

Run it as `python -m cookie_clicker_bot.presentation.capture_steps --out DIR`.
It is a documentation tool, so it uses the Selenium adapter directly and always
runs headless.
"""

import argparse
import json
import logging
from collections.abc import Callable, Sequence
from pathlib import Path

from selenium.webdriver.remote.webdriver import WebDriver

from cookie_clicker_bot.application.use_cases.bot_core import (
    click_cookie,
    get_cookie_count,
    open_game,
    select_language,
)
from cookie_clicker_bot.application.use_cases.run_bot import run_bot
from cookie_clicker_bot.application.use_cases.store import (
    buy_upgrade,
    get_store_items,
)
from cookie_clicker_bot.constants import (
    CAPTURE_CLICK_COUNT,
    CAPTURE_MAX_BURSTS,
    CLICKS_PER_BURST,
    RESULT_LABEL,
    RUN_DURATION_SECONDS,
    SCREENSHOT_BUY_UPGRADE,
    SCREENSHOT_CLICK_COOKIE,
    SCREENSHOT_OPEN_GAME,
    SCREENSHOT_READ_COUNT,
    SCREENSHOT_RESULT,
    STEPS_RECORD_FILE,
)
from cookie_clicker_bot.domain.store_item import StoreItem, choose_upgrade
from cookie_clicker_bot.infrastructure.selenium_game import (
    SeleniumGame,
    create_chrome_driver,
)
from cookie_clicker_bot.infrastructure.system_clock import SystemClock

DriverFactory = Callable[[bool], WebDriver]

_logger = logging.getLogger(__name__)


class StepUnreachableError(RuntimeError):
    """@brief Raised when a lecture step cannot be reached or does not succeed."""


def _parse_arguments(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="capture_steps",
        description="Play the five lecture steps and save a screenshot after each.",
    )
    parser.add_argument(
        "--out", type=Path, required=True, help="folder for the screenshots"
    )
    parser.add_argument(
        "--duration",
        type=float,
        default=RUN_DURATION_SECONDS,
        help="seconds of the final run (default: %(default)s)",
    )
    return parser.parse_args(argv)


def _click_until_affordable(game: SeleniumGame) -> StoreItem:
    """@brief Click in bursts until a product can be bought, within a fixed bound."""
    for _ in range(CAPTURE_MAX_BURSTS):
        item = choose_upgrade(get_store_items(game))
        if item is not None:
            return item
        click_cookie(game, CLICKS_PER_BURST)
    raise StepUnreachableError(
        f"no product became affordable within {CAPTURE_MAX_BURSTS} bursts of clicks"
    )


def _buy_first_product(game: SeleniumGame) -> StoreItem:
    item = _click_until_affordable(game)
    if not buy_upgrade(game, item):
        raise StepUnreachableError(
            f"buying product {item.index} did not raise the owned amount"
        )
    return item


def _write_record(
    path: Path, count: int, item: StoreItem, cps: str, duration: float
) -> None:
    record = {
        "cookie_count": count,
        "bought": {"index": item.index, "price": item.price},
        "cps": cps,
        "duration_seconds": duration,
    }
    path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8", newline="\n")


def _capture(game: SeleniumGame, out: Path, duration: float) -> str:
    """@brief Play the five steps, saving a screenshot after each; return the cps."""
    open_game(game)
    game.save_screenshot(out / SCREENSHOT_OPEN_GAME)

    select_language(game)
    click_cookie(game, CAPTURE_CLICK_COUNT)
    game.save_screenshot(out / SCREENSHOT_CLICK_COOKIE)

    count = get_cookie_count(game)
    _logger.info("Read %d cookies", count)
    game.save_screenshot(out / SCREENSHOT_READ_COUNT)

    item = _buy_first_product(game)
    game.save_screenshot(out / SCREENSHOT_BUY_UPGRADE)

    cps = str(run_bot(game, SystemClock(), duration))
    game.save_screenshot(out / SCREENSHOT_RESULT)

    _write_record(out / STEPS_RECORD_FILE, count, item, cps, duration)
    return cps


def main(
    argv: Sequence[str] | None = None,
    driver_factory: DriverFactory = create_chrome_driver,
) -> int:
    """@brief Capture one screenshot per lecture step and print the result.
    @param argv The command line arguments, or None to read them from the process.
    @param driver_factory Builds the web driver; replaced in tests so no browser starts.
    @return The process exit code, zero on success.
    @throws StepUnreachableError When a step cannot be reached.
    """
    arguments = _parse_arguments(argv)
    game = SeleniumGame(driver_factory(True))
    try:
        cps = _capture(game, arguments.out, arguments.duration)
        print(f"{RESULT_LABEL} : {cps}")
    finally:
        game.close()
    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    raise SystemExit(main())
