# Step 3: read the count

🌐 **English** · [Dansk](Step-3-Read-The-Count-da) · [Bahasa Melayu](Step-3-Read-The-Count-ms)

`get_cookie_count` reads the first line of the counter and turns it into a whole number. The game writes `12,345` and, for big amounts, `1.234 million`.

**Screenshot**

![Step 3: read the count](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/raw/branch/main/docs/images/step-3-read-count.png)

**Function**

```python
def get_cookie_count(game: GamePort) -> int:
    first_line = game.read_text(COOKIE_COUNTER_ID).strip().splitlines()[0]
    return parse_game_number(first_line)
```

## What we gained

- **Parse the game's own number format.** Commas group thousands and number words (`million`, `billion`, up to `decillion`) scale the value.
- **Use `Decimal`, not `float`.** A first version used `float` and `3 decillion` came out wrong; `Decimal` is exact. A failing test found it.
- **Fail with a clear error.** Text without a leading number raises `UnreadableNumberError` instead of returning a wrong value.
- **Test the edge cases.** Empty text, a plural and a singular (`1 cookie`), unknown words and rounding are all in the tests.

Next: [Step 4: buy upgrades](Step-4-Buy-Upgrades)
