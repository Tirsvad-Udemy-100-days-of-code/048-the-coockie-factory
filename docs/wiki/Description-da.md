# Beskrivelse

🌐 [English](Description) · **Dansk** · [Bahasa Melayu](Description-ms)

## Hvad projektet er

Botten åbner Cookie Clicker i Chrome, klikker på den store cookie så hurtigt spillet tillader, besøger butikken hvert femte sekund og køber det dyreste produkt, den har råd til. Efter 300 sekunder aflæser den cookies i sekundet og skriver `Result : <cps>`.

## Hvordan koden er lagdelt

Koden følger en lille Clean Architecture, så beslutningerne kan testes uden en browser.

| Lag | Indeholder | Kender Selenium? |
| --- | --- | --- |
| `domain` | Taltolkning (`parse_game_number`) og købsvalget (`choose_upgrade`) | Nej |
| `application` | Funktionerne for forelæsningens trin og portene `GamePort` og `Clock` | Nej |
| `infrastructure` | `SeleniumGame` (adapteren) og `SystemClock` | Ja |
| `presentation` | `main` og skærmbilledoptagelsen, kompositionsrødderne | Gennem adapteren |

`constants.py` indeholder adressen, element-id'erne, tiderne og talordene, så en ændring i spillets side er en ændring i én fil.

## Den ene afhængighed

`selenium` er den eneste runtime-afhængighed. En bot kan ikke styre en browser uden, og opgaven bruger det. Begrundelsen og de afviste muligheder står i ADR-0001 (se [Appendiks](Appendix-Documentation-da)).

## Hvad testene beviser

De 99 tests bruger et falsk spil og et falsk ur. De kører på et sekund, kræver hverken Chrome eller netværk og dækker taltolkningen, strategien, løkken og kommandolinjen. Det rigtige spil er kun afprøvet i Docker (se [trin 5](Step-5-Five-Minute-Run-da)).
