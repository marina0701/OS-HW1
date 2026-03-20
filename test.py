"""Test function to verify whether the Roman numeber was calculated correctly"""

from utils import roem


def test_roem(zahl):
    """function to test the converter."""

    tausender = zahl // 1000
    hunderter = (zahl % 1000) // 100
    zehner = (zahl % 100) // 10
    einer = zahl % 10

    print(
        f"Hunderter: {roem(hunderter * 100)}",
        f"tausender: {roem(tausender * 1000)}",
        f"Zehner: {roem(zehner * 10)}",
        f"Einer: {roem(einer)}",
        f"Gesamt: {roem(zahl)}",
    )
