# Trin 2: klik på cookien

🌐 [English](Step-2-Click-The-Cookie) · **Dansk** · [Bahasa Melayu](Step-2-Click-The-Cookie-ms)

`click_cookie` klikker et antal gange på den store cookie. Efter 15 klik viser skærmbilledet tælleren og de første cookies i bageriet.

**Skærmbillede**

![Trin 2: klik på cookien](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/raw/branch/main/docs/images/step-2-click-cookie.png)

**Funktion**

```python
def click_cookie(game: GamePort, times: int = 1) -> None:
    if times < 0:
        raise ValueError(f"times must not be negative, got {times}")
    for _ in range(times):
        game.click_element(BIG_COOKIE_ID)
```

## Hvad vi fik ud af det

- **Et rigtigt klik, ikke et script-klik.** Spillet ignorerer syntetiske klik over cirka 3 i sekundet, men tager imod cirka 50 i sekundet fra et rigtigt klik, så `SeleniumGame` bruger altid `element.click()`.
- **Pas på inddata.** Et negativt antal klik giver `ValueError`, og nul klik er tilladt; begge dele er testet.
- **Prøv igen, når siden ændrer sig.** Spillet tegner siden om ofte, så et klik på et forældet element prøves igen et par gange.

Næste: [Trin 3: læs antallet](Step-3-Read-The-Count-da)
