"""@file
@brief The port through which the bot tells the time.
"""

from typing import Protocol


class Clock(Protocol):
    """@brief A monotonic clock. The system clock implements it."""

    def monotonic(self) -> float:
        """@brief Return seconds from a fixed but arbitrary start, never going back.
        @return The seconds.
        """
        ...
