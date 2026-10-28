# Headless Chromium for the Cookie Clicker bot. GUI runs never use the host desktop.
FROM python:3.13-slim-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends chromium chromium-driver fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/chromium \
    CHROMEDRIVER=/usr/bin/chromedriver \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY src ./src
RUN python -m pip install --upgrade pip \
    && python -m pip install .

RUN useradd --create-home bot \
    && mkdir /runs \
    && chown bot /runs
USER bot

VOLUME ["/runs"]
ENTRYPOINT ["python", "-m", "cookie_clicker_bot.presentation.capture_steps"]
CMD ["--out", "/runs"]
