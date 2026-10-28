# Step 4: buy upgrades

🌐 **English** · [Dansk](Step-4-Buy-Upgrades-da) · [Bahasa Melayu](Step-4-Buy-Upgrades-ms)

`get_store_items` reads the 20 store products, `choose_upgrade` picks the most expensive one the bot can afford, and `buy_upgrade` clicks it. The screenshot shows the first cursor bought.

**Screenshot**

![Step 4: buy upgrades](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/raw/branch/main/docs/images/step-4-buy-upgrade.png)

**Function**

```python
def choose_upgrade(items: Sequence[StoreItem]) -> StoreItem | None:
    affordable = [item for item in items if item.is_affordable]
    if not affordable:
        return None
    return max(affordable, key=lambda item: (item.price, item.index))
```

## What we gained

- **Keep the decision pure.** `choose_upgrade` takes plain `StoreItem` values and returns one, so it is tested with no game at all (ties, none affordable, empty list).
- **Confirm the result, do not assume it.** `buy_upgrade` checks that the owned amount (`productOwned<N>`) went up. Checking the cookie count first was wrong: the count keeps rising while the bot clicks.
- **The page lags behind.** The live run showed that about 40 percent of the purchase attempts fail because the store flags are read just before the game redraws. The bot logs it and tries again at the next store check.
- **The real game finds what fakes cannot.** The stale-element retry and the owned-amount check both came from running in Docker.

Next: [Step 5: the five-minute run](Step-5-Five-Minute-Run)
