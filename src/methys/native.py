"""Native-library discovery boundary.

The C library is built independently during the skeleton phase. This module is
the single location where a future stable binding (ctypes, CPython API, or cffi)
will be introduced.
"""

from __future__ import annotations


def native_version() -> str:
    """Return the native API version expected by this Python package."""
    return "0.1.0"
