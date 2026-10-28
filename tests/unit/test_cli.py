"""@file
@brief Tests of the command line entry point; no browser is started.
"""

from decimal import Decimal
from typing import cast

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from cookie_clicker_bot.application.ports.clock import Clock
from cookie_clicker_bot.application.ports.game_port import GamePort
from cookie_clicker_bot.constants import RUN_DURATION_SECONDS
from cookie_clicker_bot.presentation import cli


class FakeDriver:
    def __init__(self) -> None:
        self.quit_calls = 0

    def quit(self) -> None:
        self.quit_calls += 1


class Recorder:
    """Stands in for the use cases and the driver factory and records the calls."""

    def __init__(self) -> None:
        self.driver = FakeDriver()
        self.headless: list[bool] = []
        self.durations: list[float] = []
        self.steps: list[str] = []
        self.error: Exception | None = None

    def driver_factory(self, headless: bool) -> WebDriver:
        self.headless.append(headless)
        return cast(WebDriver, self.driver)

    def open_game(self, game: GamePort) -> None:
        self.steps.append("open")

    def select_language(self, game: GamePort) -> None:
        self.steps.append("language")

    def run_bot(self, game: GamePort, clock: Clock, duration: float) -> Decimal:
        self.steps.append("run")
        self.durations.append(duration)
        if self.error is not None:
            raise self.error
        return Decimal("12.5")


@pytest.fixture
def recorder(monkeypatch: pytest.MonkeyPatch) -> Recorder:
    rec = Recorder()
    monkeypatch.setattr(cli, "open_game", rec.open_game)
    monkeypatch.setattr(cli, "select_language", rec.select_language)
    monkeypatch.setattr(cli, "run_bot", rec.run_bot)
    return rec


def test_main_runs_the_steps_prints_the_result_and_closes(
    recorder: Recorder, capsys: pytest.CaptureFixture[str]
) -> None:
    assert cli.main([], recorder.driver_factory) == 0
    assert recorder.steps == ["open", "language", "run"]
    assert capsys.readouterr().out == "Result : 12.5\n"
    assert recorder.driver.quit_calls == 1


def test_main_uses_the_default_duration_and_a_visible_browser(
    recorder: Recorder,
) -> None:
    cli.main([], recorder.driver_factory)
    assert recorder.durations == [RUN_DURATION_SECONDS]
    assert recorder.headless == [False]


def test_main_passes_the_headless_flag_and_duration(recorder: Recorder) -> None:
    cli.main(["--headless", "--duration", "30"], recorder.driver_factory)
    assert recorder.durations == [30.0]
    assert recorder.headless == [True]


def test_main_closes_the_browser_when_the_run_fails(
    recorder: Recorder, capsys: pytest.CaptureFixture[str]
) -> None:
    recorder.error = RuntimeError("boom")
    with pytest.raises(RuntimeError, match="boom"):
        cli.main([], recorder.driver_factory)
    assert recorder.driver.quit_calls == 1
    assert capsys.readouterr().out == ""
