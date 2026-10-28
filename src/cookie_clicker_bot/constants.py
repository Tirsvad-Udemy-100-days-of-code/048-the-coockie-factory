"""@file
@brief Constants shared by every layer of the bot.

Game specific values (URL, element ids) are added with the code that uses them.
"""

## Seconds the bot plays before it reads the cookies per second (lecture step 5).
RUN_DURATION_SECONDS: int = 300

## Seconds between two looks at the store while the bot keeps clicking.
STORE_CHECK_INTERVAL_SECONDS: int = 5

## Seconds to wait for an element before the bot gives up.
ELEMENT_TIMEOUT_SECONDS: int = 20
