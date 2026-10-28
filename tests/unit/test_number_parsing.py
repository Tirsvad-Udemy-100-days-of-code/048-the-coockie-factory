"""@file
@brief Tests of parse_game_number.
"""

from decimal import Decimal

import pytest

from cookie_clicker_bot.domain.errors import UnreadableNumberError
from cookie_clicker_bot.domain.number_parsing import (
    parse_game_decimal,
    parse_game_number,
)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("0", 0),
        ("1 cookie", 1),
        ("15 cookies", 15),
        ("12,345 cookies", 12345),
        ("1,234,567", 1234567),
    ],
)
def test_parse_plain_amounts(text: str, expected: int) -> None:
    assert parse_game_number(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("1.234 million", 1_234_000),
        ("2 billion", 2_000_000_000),
        ("1.500 Thousand", 1500),
        ("3 decillion", 3 * 10**33),
    ],
)
def test_parse_amounts_with_number_word(text: str, expected: int) -> None:
    assert parse_game_number(text) == expected


def test_parse_ignores_unknown_word_after_the_number() -> None:
    assert parse_game_number("42 bakers") == 42


def test_parse_rounds_decimals() -> None:
    assert parse_game_number("7.6 cookies") == 8


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("0.1", Decimal("0.1")),
        ("1,234.5", Decimal("1234.5")),
        ("1.234 million", Decimal("1234000")),
        ("7", Decimal(7)),
    ],
)
def test_parse_decimal_keeps_the_decimals(text: str, expected: Decimal) -> None:
    assert parse_game_decimal(text) == expected


def test_parse_decimal_rejects_text_without_a_number() -> None:
    with pytest.raises(UnreadableNumberError):
        parse_game_decimal("none")


@pytest.mark.parametrize("text", ["", "cookies", "-5", "per second: 3"])
def test_parse_rejects_text_without_a_leading_number(text: str) -> None:
    with pytest.raises(UnreadableNumberError):
        parse_game_number(text)
