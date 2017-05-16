"""Tests for fibonacci"""


def test_fibonacci():
    """Test fibonacci"""
    from series import fibonacci
    assert fibonacci(7) == 13


def test_lucas():
    """Test lucas"""
    from series import lucas
    assert lucas(7) == 29
