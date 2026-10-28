# Trin 5: kørslen på fem minutter

🌐 [English](Step-5-Five-Minute-Run) · **Dansk** · [Bahasa Melayu](Step-5-Five-Minute-Run-ms)

`run_bot` spiller i 300 sekunder i én løkke: en byge på 20 klik, og hvert 5. sekund et besøg i butikken. Til sidst læser `get_cps` cookies i sekundet. Kørslen på skærmbilledet nåede **16,6 cookies i sekundet** med 26 markører og 14 bedstemødre.

**Skærmbillede**

![Trin 5: kørslen på fem minutter](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/raw/branch/main/docs/images/step-5-result.png)

**Funktion**

```python
while now - start < duration_seconds:
    click_cookie(game, CLICKS_PER_BURST)
    now = clock.monotonic()
    if now >= next_store_check:
        _buy_while_affordable(game)
        next_store_check = now + STORE_CHECK_INTERVAL_SECONDS
```

## Hvad vi fik ud af det

- **Én løkke, ingen tråde.** Den tidligere løsning brugte to tråde og en ekstra pakke. Én løkke er lettere at læse, kræver ingen ekstra afhængighed og er let at teste.
- **Injicér uret.** `run_bot` får et `Clock`, så et falsk ur tester en kørsel på 300 sekunder på millisekunder.
- **Kør GUI'en i Docker.** Headless Chromium i en container tager aldrig din mus eller dit tastatur, og skærmbillederne og loggen kommer ud som filer.
- **Videre derfra.** Køb efter pris pr. cookie i sekundet, køb opgraderingerne og klik på den gyldne cookie: hver er en ny funktion bag de samme porte.
