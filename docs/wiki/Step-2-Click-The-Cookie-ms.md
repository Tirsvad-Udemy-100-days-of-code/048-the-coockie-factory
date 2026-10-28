# Langkah 2: klik kuki

🌐 [English](Step-2-Click-The-Cookie) · [Dansk](Step-2-Click-The-Cookie-da) · **Bahasa Melayu**

`click_cookie` mengklik kuki besar beberapa kali. Selepas 15 klik, tangkapan skrin menunjukkan pembilang dan kuki pertama di kedai roti.

**Tangkapan skrin**

![Langkah 2: klik kuki](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/raw/branch/main/docs/images/step-2-click-cookie.png)

**Fungsi**

```python
def click_cookie(game: GamePort, times: int = 1) -> None:
    if times < 0:
        raise ValueError(f"times must not be negative, got {times}")
    for _ in range(times):
        game.click_element(BIG_COOKIE_ID)
```

## Apa yang kami peroleh

- **Klik sebenar, bukan klik skrip.** Permainan mengabaikan klik sintetik melebihi kira-kira 3 sesaat tetapi menerima kira-kira 50 sesaat daripada klik sebenar, jadi `SeleniumGame` sentiasa menggunakan `element.click()`.
- **Kawal input.** Bilangan klik negatif menimbulkan `ValueError`, dan sifar klik dibenarkan; kedua-duanya diuji.
- **Cuba semula apabila halaman berubah.** Permainan melukis semula halamannya dengan kerap, jadi klik pada elemen yang usang dicuba semula beberapa kali.

Seterusnya: [Langkah 3: baca bilangan](Step-3-Read-The-Count-ms)
