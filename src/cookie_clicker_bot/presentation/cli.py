"""@file
@brief Command line entry point and composition root of the bot.
"""

import argparse
from collections.abc import Callable, Sequence

from selenium.webdriver.remote.webdriver import WebDriver

from cookie_clicker_bot.application.use_cases.bot_core import open_game, select_language
from cookie_clicker_bot.application.use_cases.run_bot import run_bot
from cookie_clicker_bot.constants import RESULT_LABEL, RUN_DURATION_SECONDS
from cookie_clicker_bot.infrastructure.selenium_game import (
    SeleniumGame,
    create_chrome_driver,
)
from cookie_clicker_bot.infrastructure.system_clock import SystemClock

DriverFactory = Callable[[bool], WebDriver]


def _parse_arguments(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="cookie_clicker_bot", description="Play Cookie Clicker."
    )
    parser.add_argument(
        "--headless", action="store_true", help="run Chrome without a window"
    )
    parser.add_argument(
        "--duration",
        type=float,
        default=RUN_DURATION_SECONDS,
        help="seconds to play (default: %(default)s)",
    )
    return parser.parse_args(argv)


def main(
    argv: Sequence[str] | None = None,
    driver_factory: DriverFactory = create_chrome_driver,
) -> int:
    """@brief Start the browser, run the bot, print the result and close the browser.
    @param argv The command line arguments, or None to read them from the process.
    @param driver_factory Builds the web driver; replaced in tests so no browser starts.
    @return The process exit code, zero on success.
    @throws ValueError When the duration is zero or negative.
    """
    arguments = _parse_arguments(argv)
    game = SeleniumGame(driver_factory(arguments.headless))
    try:
        open_game(game)
        select_language(game)
        cps = run_bot(game, SystemClock(), arguments.duration)
        print(f"{RESULT_LABEL} : {cps}")
    finally:
        game.close()
    return 0
