"""@file
@brief The Clock port backed by the operating system.
"""

import time


class SystemClock:
    """@brief Reads the real monotonic clock."""

    def monotonic(self) -> float:
        """@brief Return seconds from a fixed but arbitrary start, never going back.
        @return The seconds.
        """
        return time.monotonic()
