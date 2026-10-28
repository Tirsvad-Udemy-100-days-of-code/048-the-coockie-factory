# Huraian

🌐 [English](Description) · [Dansk](Description-da) · **Bahasa Melayu**

## Apa itu projek ini

Bot membuka Cookie Clicker dalam Chrome, mengklik kuki besar secepat yang dibenarkan permainan, melawat kedai setiap lima saat dan membeli produk termahal yang mampu dibelinya. Selepas 300 saat ia membaca kuki sesaat dan mencetak `Result : <cps>`.

## Bagaimana kod disusun berlapis

Kod mengikut Clean Architecture yang kecil, supaya keputusan boleh diuji tanpa pelayar.

| Lapisan | Mengandungi | Mengenali Selenium? |
| --- | --- | --- |
| `domain` | Pentafsiran nombor (`parse_game_number`) dan pilihan pembelian (`choose_upgrade`) | Tidak |
| `application` | Fungsi bagi langkah kuliah dan port `GamePort` dan `Clock` | Tidak |
| `infrastructure` | `SeleniumGame` (penyesuai) dan `SystemClock` | Ya |
| `presentation` | `main` dan penangkapan tangkapan skrin, akar komposisi | Melalui penyesuai |

`constants.py` menyimpan alamat, id elemen, masa dan perkataan nombor, jadi perubahan pada halaman permainan hanyalah perubahan dalam satu fail.

## Satu kebergantungan

`selenium` ialah satu-satunya kebergantungan masa jalan. Bot tidak boleh mengawal pelayar tanpanya, dan tugasan menggunakannya. Sebab dan pilihan yang ditolak ada dalam ADR-0001 (lihat [Lampiran](Appendix-Documentation-ms)).

## Apa yang dibuktikan oleh ujian

99 ujian menggunakan permainan palsu dan jam palsu. Ia berjalan dalam satu saat, tidak memerlukan Chrome atau rangkaian, dan merangkumi pentafsir, strategi, gelung dan baris arahan. Permainan sebenar hanya diuji dalam Docker (lihat [langkah 5](Step-5-Five-Minute-Run-ms)).
