"""@file
@brief Tests of the screenshot capture entry point; no browser is started.
"""

import json
from decimal import Decimal
from pathlib import Path
from typing import cast

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from cookie_clicker_bot.application.ports.clock import Clock
from cookie_clicker_bot.application.ports.game_port import GamePort
from cookie_clicker_bot.constants import (
    CAPTURE_CLICK_COUNT,
    CAPTURE_MAX_BURSTS,
    CLICKS_PER_BURST,
    RUN_DURATION_SECONDS,
)
from cookie_clicker_bot.domain.store_item import StoreItem
from cookie_clicker_bot.presentation import capture_steps

STEP_FILES = [
    "step-1-open-game.png",
    "step-2-click-cookie.png",
    "step-3-read-count.png",
    "step-4-buy-upgrade.png",
    "step-5-result.png",
]


class FakeDriver:
    def __init__(self, events: list[str]) -> None:
        self.events = events
        self.quit_calls = 0

    def save_screenshot(self, filename: str) -> bool:
        Path(filename).write_bytes(b"png")
        self.events.append(f"shot:{Path(filename).name}")
        return True

    def quit(self) -> None:
        self.quit_calls += 1


class Script:
    """Stands in for the use cases and the driver factory and records the order."""

    def __init__(self) -> None:
        self.events: list[str] = []
        self.driver = FakeDriver(self.events)
        self.headless: list[bool] = []
        self.durations: list[float] = []
        self.clicks: list[int] = []
        self.affordable_after_bursts = 2
        self.store_reads = 0
        self.purchase_works = True

    def driver_factory(self, headless: bool) -> WebDriver:
        self.headless.append(headless)
        return cast(WebDriver, self.driver)

    def open_game(self, game: GamePort) -> None:
        self.events.append("open")

    def select_language(self, game: GamePort) -> None:
        self.events.append("language")

    def click_cookie(self, game: GamePort, times: int = 1) -> None:
        self.clicks.append(times)
        self.events.append(f"click:{times}")

    def get_cookie_count(self, game: GamePort) -> int:
        self.events.append("count")
        return 42

    def get_store_items(self, game: GamePort) -> list[StoreItem]:
        self.store_reads += 1
        affordable = len(self.clicks) - 1 >= self.affordable_after_bursts
        return [StoreItem(3, 100, affordable)]

    def buy_upgrade(self, game: GamePort, item: StoreItem) -> bool:
        self.events.append(f"buy:{item.index}")
        return self.purchase_works

    def run_bot(self, game: GamePort, clock: Clock, duration: float) -> Decimal:
        self.events.append("run")
        self.durations.append(duration)
        return Decimal("12.5")


@pytest.fixture
def script(monkeypatch: pytest.MonkeyPatch) -> Script:
    s = Script()
    for name in (
        "open_game",
        "select_language",
        "click_cookie",
        "get_cookie_count",
        "get_store_items",
        "buy_upgrade",
        "run_bot",
    ):
        monkeypatch.setattr(capture_steps, name, getattr(s, name))
    return s


def test_main_saves_one_screenshot_per_step_in_order(
    script: Script, tmp_path: Path
) -> None:
    assert capture_steps.main(["--out", str(tmp_path)], script.driver_factory) == 0
    shots = [e for e in script.events if e.startswith("shot:")]
    assert shots == ["shot:" + name for name in STEP_FILES]
    assert all((tmp_path / name).read_bytes() == b"png" for name in STEP_FILES)
    assert script.events[:5] == [
        "open",
        "shot:step-1-open-game.png",
        "language",
        f"click:{CAPTURE_CLICK_COUNT}",
        "shot:step-2-click-cookie.png",
    ]


def test_main_runs_headless_closes_and_prints_the_result(
    script: Script, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    capture_steps.main(["--out", str(tmp_path)], script.driver_factory)
    assert script.headless == [True]
    assert script.driver.quit_calls == 1
    assert capsys.readouterr().out == "Result : 12.5\n"
    assert script.durations == [RUN_DURATION_SECONDS]


def test_main_writes_the_steps_record(script: Script, tmp_path: Path) -> None:
    capture_steps.main(
        ["--out", str(tmp_path), "--duration", "30"], script.driver_factory
    )
    record = json.loads((tmp_path / "steps.json").read_text(encoding="utf-8"))
    assert record == {
        "cookie_count": 42,
        "bought": {"index": 3, "price": 100},
        "cps": "12.5",
        "duration_seconds": 30.0,
    }


def test_main_creates_the_output_folder(script: Script, tmp_path: Path) -> None:
    out = tmp_path / "nested" / "shots"
    capture_steps.main(["--out", str(out)], script.driver_factory)
    assert (out / STEP_FILES[0]).exists()


def test_main_clicks_in_bursts_until_a_product_is_affordable(
    script: Script, tmp_path: Path
) -> None:
    capture_steps.main(["--out", str(tmp_path)], script.driver_factory)
    assert script.clicks == [CAPTURE_CLICK_COUNT] + [CLICKS_PER_BURST] * 2


def test_main_raises_when_nothing_becomes_affordable(
    script: Script, tmp_path: Path
) -> None:
    script.affordable_after_bursts = CAPTURE_MAX_BURSTS + 10
    with pytest.raises(capture_steps.StepUnreachableError, match="affordable"):
        capture_steps.main(["--out", str(tmp_path)], script.driver_factory)
    assert script.store_reads == CAPTURE_MAX_BURSTS
    assert script.driver.quit_calls == 1
    assert not (tmp_path / "step-4-buy-upgrade.png").exists()


def test_main_raises_when_the_purchase_does_not_go_through(
    script: Script, tmp_path: Path
) -> None:
    script.purchase_works = False
    with pytest.raises(capture_steps.StepUnreachableError, match="owned amount"):
        capture_steps.main(["--out", str(tmp_path)], script.driver_factory)
    assert script.driver.quit_calls == 1
    assert not (tmp_path / "steps.json").exists()


def test_main_requires_the_out_argument(script: Script) -> None:
    with pytest.raises(SystemExit):
        capture_steps.main([], script.driver_factory)
