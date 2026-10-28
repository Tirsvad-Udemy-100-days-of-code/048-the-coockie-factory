# Install

🌐 **English** · [Dansk](Install-da) · [Bahasa Melayu](Install-ms)

## You need

- Python 3.13 or newer.
- Google Chrome (Selenium Manager downloads the driver). Not needed for the tests.
- Docker, only to repeat the headless run and the screenshots.

## Create and use a local `.venv`

The first block is for Windows PowerShell, the second for Linux and macOS. Leave the environment with `deactivate`.

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

## Run the bot and the tests

```bash
python -m cookie_clicker_bot
python -m cookie_clicker_bot --headless --duration 60
python -m pytest
```

## Repeat the screenshots in Docker

The run is headless, so it never takes your mouse or keyboard. The screenshots and `steps.json` land in `runs/`.

```bash
docker build -t cookie-clicker-bot -f docker/Dockerfile .
docker run --rm -v "$(pwd)/runs:/runs" cookie-clicker-bot --out /runs
```
