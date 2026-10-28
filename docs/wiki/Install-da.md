# Installation

🌐 [English](Install) · **Dansk** · [Bahasa Melayu](Install-ms)

## Du skal bruge

- Python 3.13 eller nyere.
- Google Chrome (Selenium Manager henter driveren). Ikke nødvendig til testene.
- Docker, kun for at gentage den headless kørsel og skærmbillederne.

## Opret og brug et lokalt `.venv`

Første blok er til Windows PowerShell, anden til Linux og macOS. Forlad miljøet med `deactivate`.

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

## Kør botten og testene

```bash
python -m cookie_clicker_bot
python -m cookie_clicker_bot --headless --duration 60
python -m pytest
```

## Gentag skærmbillederne i Docker

Kørslen er headless, så den tager aldrig din mus eller dit tastatur. Skærmbillederne og `steps.json` havner i `runs/`.

```bash
docker build -t cookie-clicker-bot -f docker/Dockerfile .
docker run --rm -v "$(pwd)/runs:/runs" cookie-clicker-bot --out /runs
```
