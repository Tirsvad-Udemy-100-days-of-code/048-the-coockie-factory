# Description

🌐 **English** · [Dansk](Description-da) · [Bahasa Melayu](Description-ms)

## What the project is

The bot opens Cookie Clicker in Chrome, clicks the big cookie as fast as the game allows, visits the store every five seconds and buys the most expensive product it can afford. After 300 seconds it reads the cookies per second and prints `Result : <cps>`.

## How the code is layered

The code follows a small Clean Architecture, so the decisions can be tested without a browser.

| Layer | Holds | Knows about Selenium? |
| --- | --- | --- |
| `domain` | Number parsing (`parse_game_number`) and the purchase choice (`choose_upgrade`) | No |
| `application` | The lecture step functions and the ports `GamePort` and `Clock` | No |
| `infrastructure` | `SeleniumGame` (the adapter) and `SystemClock` | Yes |
| `presentation` | `main` and the screenshot capture, the composition roots | Through the adapter |

`constants.py` holds the address, the element ids, the timings and the number words, so a change in the game's page is a change in one file.

## The one dependency

`selenium` is the only runtime dependency. A bot cannot drive a browser without it, and the assignment uses it. The reasons and the options that were rejected are in ADR-0001 (see [Appendix](Appendix-Documentation)).

## What the tests prove

The 99 tests use a fake game and a fake clock. They run in a second, need no Chrome and no network, and cover the parser, the strategy, the loop and the command line. The real game was exercised only in Docker (see [step 5](Step-5-Five-Minute-Run)).
