# Trin 4: køb opgraderinger

🌐 [English](Step-4-Buy-Upgrades) · **Dansk** · [Bahasa Melayu](Step-4-Buy-Upgrades-ms)

`get_store_items` læser butikkens 20 produkter, `choose_upgrade` vælger det dyreste, botten har råd til, og `buy_upgrade` klikker på det. Skærmbilledet viser den første markør, der er købt.

**Skærmbillede**

![Trin 4: køb opgraderinger](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/raw/branch/main/docs/images/step-4-buy-upgrade.png)

**Funktion**

```python
def choose_upgrade(items: Sequence[StoreItem]) -> StoreItem | None:
    affordable = [item for item in items if item.is_affordable]
    if not affordable:
        return None
    return max(affordable, key=lambda item: (item.price, item.index))
```

## Hvad vi fik ud af det

- **Hold beslutningen ren.** `choose_upgrade` tager almindelige `StoreItem`-værdier og returnerer én, så den testes uden noget spil (lige priser, intet overkommeligt, tom liste).
- **Bekræft resultatet, antag det ikke.** `buy_upgrade` tjekker, at det ejede antal (`productOwned<N>`) steg. At tjekke antallet af cookies først var forkert: antallet stiger, mens botten klikker.
- **Siden halter bagefter.** Den rigtige kørsel viste, at cirka 40 procent af købsforsøgene mislykkes, fordi butikkens markeringer læses lige før spillet tegner om. Botten logger det og prøver igen ved næste butiksbesøg.
- **Det rigtige spil finder det, falske ikke kan.** Genforsøget ved forældede elementer og tjekket af ejet antal kom begge fra kørsler i Docker.

Næste: [Trin 5: kørslen på fem minutter](Step-5-Five-Minute-Run-da)
