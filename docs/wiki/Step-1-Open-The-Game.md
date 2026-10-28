# Step 1: open the game

🌐 **English** · [Dansk](Step-1-Open-The-Game-da) · [Bahasa Melayu](Step-1-Open-The-Game-ms)

The bot starts Chrome, loads the game and waits until the language prompt is on the page. Then it picks English, which makes the big cookie playable.

**Screenshot**

![Step 1: open the game](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/raw/branch/main/docs/images/step-1-open-game.png)

**Function**

```python
def open_game(game: GamePort) -> None:
    game.open_page(GAME_URL)
    game.wait_for_element(LANGUAGE_BUTTON_PREFIX + LANGUAGE_CODE)


def select_language(game: GamePort) -> None:
    game.click_element(LANGUAGE_BUTTON_PREFIX + LANGUAGE_CODE)
    game.wait_for_element(BIG_COOKIE_ID)
```

## What we gained

- **Wait for an element, do not sleep.** `WebDriverWait` returns as soon as the element exists, so the bot is fast when the page is fast and patient when it is slow.
- **Selenium Manager** finds the matching Chrome driver, so there is no manual download.
- **A port keeps Selenium out of the rules.** `open_game` only talks to `GamePort`, so a fake game tests it without a browser.
- **One place for the page's details.** The address and the element ids are in `constants.py`.

Next: [Step 2: click the cookie](Step-2-Click-The-Cookie)
