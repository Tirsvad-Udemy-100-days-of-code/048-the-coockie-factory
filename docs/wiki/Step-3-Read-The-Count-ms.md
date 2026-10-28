# Langkah 3: baca bilangan

🌐 [English](Step-3-Read-The-Count) · [Dansk](Step-3-Read-The-Count-da) · **Bahasa Melayu**

`get_cookie_count` membaca baris pertama pembilang dan menukarkannya kepada nombor bulat. Permainan menulis `12,345` dan, bagi jumlah besar, `1.234 million`.

**Tangkapan skrin**

![Langkah 3: baca bilangan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/raw/branch/main/docs/images/step-3-read-count.png)

**Fungsi**

```python
def get_cookie_count(game: GamePort) -> int:
    first_line = game.read_text(COOKIE_COUNTER_ID).strip().splitlines()[0]
    return parse_game_number(first_line)
```

## Apa yang kami peroleh

- **Tafsir format nombor permainan sendiri.** Koma mengumpulkan ribuan dan perkataan nombor (`million`, `billion`, hingga `decillion`) menskalakan nilai.
- **Guna `Decimal`, bukan `float`.** Versi pertama menggunakan `float` dan `3 decillion` menjadi salah; `Decimal` tepat. Ujian yang gagal menemuinya.
- **Gagal dengan ralat yang jelas.** Teks tanpa nombor di hadapan menimbulkan `UnreadableNumberError` dan bukannya nilai yang salah.
- **Uji kes tepi.** Teks kosong, tunggal dan jamak (`1 cookie`), perkataan tidak dikenali dan pembundaran semuanya ada dalam ujian.

Seterusnya: [Langkah 4: beli peningkatan](Step-4-Buy-Upgrades-ms)
