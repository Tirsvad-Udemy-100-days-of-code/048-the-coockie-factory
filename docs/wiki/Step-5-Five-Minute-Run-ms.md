# Langkah 5: larian lima minit

🌐 [English](Step-5-Five-Minute-Run) · [Dansk](Step-5-Five-Minute-Run-da) · **Bahasa Melayu**

`run_bot` bermain selama 300 saat dalam satu gelung: satu rentetan 20 klik, kemudian setiap saat satu lawatan ke kedai: peti peningkatan dahulu, kemudian paling banyak satu produk. Pada akhirnya `get_cps` membaca kuki sesaat. Larian dalam tangkapan skrin mencapai **29 kuki sesaat** dengan 29 kursor, 17 nenek dan 2 peningkatan (keluaran pertama mencapai 16.6).

**Tangkapan skrin**

![Langkah 5: larian lima minit](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/raw/branch/main/docs/images/step-5-result.png)

**Fungsi**

```python
while now - start < duration_seconds:
    click_cookie(game, CLICKS_PER_BURST)
    now = clock.monotonic()
    if now >= next_store_check:
        _buy_while_affordable(game)
        next_store_check = now + STORE_CHECK_INTERVAL_SECONDS
```

## Apa yang kami peroleh

- **Satu gelung, tiada thread.** Penyelesaian terdahulu menggunakan dua thread dan satu pakej tambahan. Satu gelung lebih mudah dibaca, tidak memerlukan kebergantungan tambahan dan mudah diuji.
- **Suntik jam.** `run_bot` menerima `Clock`, jadi jam palsu menguji larian 300 saat dalam milisaat.
- **Jalankan GUI dalam Docker.** Chromium tanpa kepala dalam bekas tidak pernah mengambil tetikus atau papan kekunci anda, dan tangkapan skrin serta log keluar sebagai fail.
- **Langkah seterusnya.** Beli mengikut kos setiap kuki sesaat dan klik kuki emas: setiap satu ialah fungsi baharu di belakang port yang sama.
