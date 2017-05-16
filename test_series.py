"""Tests for the series functions."""
import pytest


PARAMS_TABLE = [
    (0, 0, 1, 0),
    (1, 1, 2, 2),
    (2, 2, 3, 5),
    (3, 3, 4, 11),
    (4, 2, 5, 19),
    (0, 1, 2, 1),
    (1, 1, 3, 3),
    (2, 1, 4, 5),
    (3, 1, 5, 11),
    (4, 1, 5, 17),
]




def test_fibonacci():
    """Test fibonacci"""
    from series import fibonacci
    assert fibonacci(7) == 13


def test_lucas():
    """Test lucas"""
    from series import lucas
    assert lucas(7) == 29


@pytest.mark.parametrize('l, m, n, result', PARAMS_TABLE)
def test_sum_series(l, m, n, result):
    """Test sum series function"""
    from series import sum_series
    assert sum_series(l, m, n) == result

