# Trin 1: åbn spillet

🌐 [English](Step-1-Open-The-Game) · **Dansk** · [Bahasa Melayu](Step-1-Open-The-Game-ms)

Botten starter Chrome, indlæser spillet og venter, til sprogvalget er på siden. Derefter vælger den engelsk, så den store cookie kan bruges.

**Skærmbillede**

![Trin 1: åbn spillet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/raw/branch/main/docs/images/step-1-open-game.png)

**Funktion**

```python
def open_game(game: GamePort) -> None:
    game.open_page(GAME_URL)
    game.wait_for_element(LANGUAGE_BUTTON_PREFIX + LANGUAGE_CODE)


def select_language(game: GamePort) -> None:
    game.click_element(LANGUAGE_BUTTON_PREFIX + LANGUAGE_CODE)
    game.wait_for_element(BIG_COOKIE_ID)
```

## Hvad vi fik ud af det

- **Vent på et element, sov ikke.** `WebDriverWait` vender tilbage, så snart elementet findes, så botten er hurtig, når siden er hurtig, og tålmodig, når den er langsom.
- **Selenium Manager** finder den rigtige Chrome-driver, så der ikke skal hentes noget manuelt.
- **En port holder Selenium ude af reglerne.** `open_game` taler kun med `GamePort`, så et falsk spil kan teste den uden browser.
- **Ét sted til sidens detaljer.** Adressen og element-id'erne står i `constants.py`.

Næste: [Trin 2: klik på cookien](Step-2-Click-The-Cookie-da)
