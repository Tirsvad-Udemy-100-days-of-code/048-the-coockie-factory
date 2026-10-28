# Trin 3: læs antallet

🌐 [English](Step-3-Read-The-Count) · **Dansk** · [Bahasa Melayu](Step-3-Read-The-Count-ms)

`get_cookie_count` læser tællerens første linje og gør den til et heltal. Spillet skriver `12,345` og, ved store beløb, `1.234 million`.

**Skærmbillede**

![Trin 3: læs antallet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/raw/branch/main/docs/images/step-3-read-count.png)

**Funktion**

```python
def get_cookie_count(game: GamePort) -> int:
    first_line = game.read_text(COOKIE_COUNTER_ID).strip().splitlines()[0]
    return parse_game_number(first_line)
```

## Hvad vi fik ud af det

- **Læs spillets eget talformat.** Kommaer grupperer tusinder, og talord (`million`, `billion`, op til `decillion`) skalerer værdien.
- **Brug `Decimal`, ikke `float`.** En første version brugte `float`, og `3 decillion` blev forkert; `Decimal` er præcis. En fejlende test fandt det.
- **Fejl med en tydelig fejl.** Tekst uden et indledende tal giver `UnreadableNumberError` i stedet for en forkert værdi.
- **Test grænsetilfældene.** Tom tekst, ental og flertal (`1 cookie`), ukendte ord og afrunding er alle med i testene.

Næste: [Trin 4: køb opgraderinger](Step-4-Buy-Upgrades-da)
