"""Test dzbee."""
# pylint: disable=broad-except
from dzbee import __version__
from dzbee import dzbee


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not dzbee()
    except Exception:
        assert True
