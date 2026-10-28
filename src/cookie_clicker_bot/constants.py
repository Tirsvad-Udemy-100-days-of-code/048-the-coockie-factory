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

## Number of products in the store.
PRODUCT_COUNT: int = 20

## Element id prefix of a store product; the product index follows.
PRODUCT_ID_PREFIX: str = "product"

## Element id prefix of the price of a store product; the product index follows.
PRODUCT_PRICE_ID_PREFIX: str = "productPrice"

## Element id prefix of the owned amount of a store product; the product index follows.
PRODUCT_OWNED_ID_PREFIX: str = "productOwned"

## Reads of the owned amount after a purchase click, as the game redraws late.
OWNED_CHECK_ATTEMPTS: int = 20

## Times an action on the page is repeated after a stale or blocked element.
CLICK_RETRIES: int = 3

## Attribute that holds the CSS classes of an element.
CLASS_ATTRIBUTE: str = "class"

## Class of a product that is visible in the store.
UNLOCKED_CLASS: str = "unlocked"

## Class of a product the player can afford.
ENABLED_CLASS: str = "enabled"

## Clicks on the big cookie between two looks at the clock.
CLICKS_PER_BURST: int = 20

## Separator between the label and the amount in the cookies per second line.
CPS_SEPARATOR: str = ":"

## Label printed before the cookies per second at the end of the run.
RESULT_LABEL: str = "Result"

## Environment variable that names the Chrome binary to start.
CHROME_BIN_ENV: str = "CHROME_BIN"

## Environment variable that names the chromedriver executable to use.
CHROMEDRIVER_ENV: str = "CHROMEDRIVER"

## Screenshot file name of lecture step 1, the game opened at the language prompt.
SCREENSHOT_OPEN_GAME: str = "step-1-open-game.png"

## Screenshot file name of lecture step 2, after the first clicks on the cookie.
SCREENSHOT_CLICK_COOKIE: str = "step-2-click-cookie.png"

## Screenshot file name of lecture step 3, after the cookie count was read.
SCREENSHOT_READ_COUNT: str = "step-3-read-count.png"

## Screenshot file name of lecture step 4, after an upgrade was bought.
SCREENSHOT_BUY_UPGRADE: str = "step-4-buy-upgrade.png"

## Screenshot file name of lecture step 5, after the full run.
SCREENSHOT_RESULT: str = "step-5-result.png"

## File name of the record of what each capture step read and did.
STEPS_RECORD_FILE: str = "steps.json"

## Clicks on the big cookie in lecture step 2 of the capture.
CAPTURE_CLICK_COUNT: int = 15

## Most bursts of clicks the capture makes while it waits for an affordable product.
CAPTURE_MAX_BURSTS: int = 200

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
