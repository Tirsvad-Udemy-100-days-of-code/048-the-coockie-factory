"""@file
@brief Constants shared by every layer of the bot.
"""

## Seconds the bot plays before it reads the cookies per second (lecture step 5).
RUN_DURATION_SECONDS: int = 300

## Seconds between two looks at the store while the bot keeps clicking.
STORE_CHECK_INTERVAL_SECONDS: int = 5

## Seconds to wait for an element before the bot gives up.
ELEMENT_TIMEOUT_SECONDS: int = 20

## Address of the game the bot plays.
GAME_URL: str = "https://ozh.github.io/cookieclicker/"

## Element id prefix of the language buttons shown on the first launch.
LANGUAGE_BUTTON_PREFIX: str = "langSelect-"

## Language the bot chooses (the game's own code for English).
LANGUAGE_CODE: str = "EN"

## Element id of the big cookie that is clicked to earn cookies.
BIG_COOKIE_ID: str = "bigCookie"

## Element id of the counter that shows the cookies and the cookies per second.
COOKIE_COUNTER_ID: str = "cookies"

## Element id of the line that shows the cookies per second.
CPS_ID: str = "cookiesPerSecond"

## Number words the game prints for large amounts, with their value.
NUMBER_SCALES: dict[str, int] = {
    "thousand": 10**3,
    "million": 10**6,
    "billion": 10**9,
    "trillion": 10**12,
    "quadrillion": 10**15,
    "quintillion": 10**18,
    "sextillion": 10**21,
    "septillion": 10**24,
    "octillion": 10**27,
    "nonillion": 10**30,
    "decillion": 10**33,
}
