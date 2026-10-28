# Langkah 1: buka permainan

🌐 [English](Step-1-Open-The-Game) · [Dansk](Step-1-Open-The-Game-da) · **Bahasa Melayu**

Bot memulakan Chrome, memuatkan permainan dan menunggu sehingga pilihan bahasa muncul pada halaman. Kemudian ia memilih bahasa Inggeris, supaya kuki besar boleh dimainkan.

**Tangkapan skrin**

![Langkah 1: buka permainan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/raw/branch/main/docs/images/step-1-open-game.png)

**Fungsi**

```python
def open_game(game: GamePort) -> None:
    game.open_page(GAME_URL)
    game.wait_for_element(LANGUAGE_BUTTON_PREFIX + LANGUAGE_CODE)


def select_language(game: GamePort) -> None:
    game.click_element(LANGUAGE_BUTTON_PREFIX + LANGUAGE_CODE)
    game.wait_for_element(BIG_COOKIE_ID)
```

## Apa yang kami peroleh

- **Tunggu elemen, jangan tidur.** `WebDriverWait` kembali sebaik sahaja elemen wujud, jadi bot pantas apabila halaman pantas dan sabar apabila ia perlahan.
- **Selenium Manager** mencari pemandu Chrome yang sepadan, jadi tiada muat turun manual.
- **Port mengasingkan Selenium daripada peraturan.** `open_game` hanya bercakap dengan `GamePort`, jadi permainan palsu boleh mengujinya tanpa pelayar.
- **Satu tempat untuk butiran halaman.** Alamat dan id elemen berada dalam `constants.py`.

Seterusnya: [Langkah 2: klik kuki](Step-2-Click-The-Cookie-ms)
