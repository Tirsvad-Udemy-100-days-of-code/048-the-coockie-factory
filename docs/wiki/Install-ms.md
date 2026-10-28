# Pemasangan

🌐 [English](Install) · [Dansk](Install-da) · **Bahasa Melayu**

## Anda memerlukan

- Python 3.13 atau lebih baharu.
- Google Chrome (Selenium Manager memuat turun pemandu). Tidak diperlukan untuk ujian.
- Docker, hanya untuk mengulang larian tanpa kepala dan tangkapan skrin.

## Cipta dan guna `.venv` setempat

Blok pertama untuk Windows PowerShell, yang kedua untuk Linux dan macOS. Keluar daripada persekitaran dengan `deactivate`.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Jalankan bot dan ujian

```bash
python -m cookie_clicker_bot
python -m cookie_clicker_bot --headless --duration 60
python -m pytest
```

## Ulang tangkapan skrin dalam Docker

Larian ini tanpa kepala, jadi ia tidak mengambil tetikus atau papan kekunci anda. Tangkapan skrin dan `steps.json` disimpan dalam `runs/`.

```bash
docker build -t cookie-clicker-bot -f docker/Dockerfile .
docker run --rm -v "$(pwd)/runs:/runs" cookie-clicker-bot --out /runs
```
