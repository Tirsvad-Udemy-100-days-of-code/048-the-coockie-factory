"""@file
@brief Lets `python -m cookie_clicker_bot` start the bot.
"""

import logging

from cookie_clicker_bot.presentation.cli import main

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )
    raise SystemExit(main())
