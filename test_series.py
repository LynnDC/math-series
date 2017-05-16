"""Tests for the series functions."""
import pytest


PARAMS_TABLE = [
    (1, 2, 1, 2),
    (1, 3, 2, 3),
    (5, 4, 1, 11),
    (4, 5, 1, 7),
    (3, 6, 1, 7),
    (2, 2, 3, 3),
    (1, 2, 4, 2),
    (2, 2, 1, 1),
    (3, 2, 4, 6),
    (2, 4, 5, 5),
]


def test_fibonacci():
    """Test fibnacci"""
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
