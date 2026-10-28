# Langkah 4: beli peningkatan

🌐 [English](Step-4-Buy-Upgrades) · [Dansk](Step-4-Buy-Upgrades-da) · **Bahasa Melayu**

`get_store_items` membaca 20 produk kedai, `choose_upgrade` memilih yang termahal yang mampu dibeli bot, dan `buy_upgrade` mengkliknya. Tangkapan skrin menunjukkan kursor pertama yang dibeli.

**Tangkapan skrin**

![Langkah 4: beli peningkatan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/raw/branch/main/docs/images/step-4-buy-upgrade.png)

**Fungsi**

```python
def choose_upgrade(items: Sequence[StoreItem]) -> StoreItem | None:
    affordable = [item for item in items if item.is_affordable]
    if not affordable:
        return None
    return max(affordable, key=lambda item: (item.price, item.index))
```

## Apa yang kami peroleh

- **Pastikan keputusan bersih.** `choose_upgrade` menerima nilai `StoreItem` biasa dan memulangkan satu, jadi ia diuji tanpa permainan langsung (harga sama, tiada yang mampu dibeli, senarai kosong).
- **Sahkan hasilnya, jangan andaikan.** `buy_upgrade` menyemak bahawa jumlah dimiliki (`productOwned<N>`) bertambah. Menyemak bilangan kuki dahulu adalah salah: bilangan terus meningkat semasa bot mengklik.
- **Halaman ketinggalan.** Larian sebenar menunjukkan kira-kira 40 peratus percubaan pembelian gagal kerana bendera kedai dibaca sebelum permainan melukis semula. Bot mencatatkannya dan mencuba lagi pada lawatan kedai seterusnya.
- **Permainan sebenar menemui apa yang tidak dapat ditemui oleh yang palsu.** Percubaan semula elemen usang dan semakan jumlah dimiliki kedua-duanya datang daripada larian dalam Docker.

Seterusnya: [Langkah 5: larian lima minit](Step-5-Five-Minute-Run-ms)
