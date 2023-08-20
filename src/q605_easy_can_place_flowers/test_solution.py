""" Testing solution """

import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "flowerbed,n,expected",
    [
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([0], 1, True),
        ([1], 1, False),
        ([1], 0, True),
        ([0, 0], 0, True),
        ([0, 0], 1, True),
        ([0, 0], 2, False),
        ([0, 1], 0, True),
        ([0, 1], 1, False),
        ([0, 0, 1], 1, True),
    ],
)
def test_solution(flowerbed, n, expected):
    """
    Checking Test Cases
    """
    assert Solution().canPlaceFlowers(flowerbed, n) == expected
