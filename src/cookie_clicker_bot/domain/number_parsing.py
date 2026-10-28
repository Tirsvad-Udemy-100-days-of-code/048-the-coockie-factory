"""@file
@brief Turns the amounts the game prints ("1.234 million") into numbers.
"""

import re
from decimal import ROUND_HALF_UP, Decimal

from cookie_clicker_bot.constants import NUMBER_SCALES
from cookie_clicker_bot.domain.errors import UnreadableNumberError

_AMOUNT = re.compile(r"^\s*(\d[\d,]*(?:\.\d+)?)(?:\s+([a-z]+))?", re.IGNORECASE)


def parse_game_decimal(text: str) -> Decimal:
    """@brief Read the first amount in a text printed by the game, keeping decimals.

    The game groups thousands with commas ("12,345") and writes large amounts
    with a number word ("1.234 million"). Any other word after the number, such
    as "cookies", is ignored.

    @param text The text, for example "0.1", "1.234 million" or "12,345 cookies".
    @return The exact amount.
    @throws UnreadableNumberError When the text does not start with a number.
    """
    match = _AMOUNT.match(text)
    if match is None:
        raise UnreadableNumberError(f"No number at the start of {text!r}")
    value = Decimal(match.group(1).replace(",", ""))
    return value * NUMBER_SCALES.get((match.group(2) or "").lower(), 1)


def parse_game_number(text: str) -> int:
    """@brief Read the first amount in a text printed by the game as a whole number.
    @param text The text, for example "1.234 million" or "12,345 cookies".
    @return The amount, rounded to a whole number.
    @throws UnreadableNumberError When the text does not start with a number.
    """
    return int(parse_game_decimal(text).to_integral_value(rounding=ROUND_HALF_UP))
