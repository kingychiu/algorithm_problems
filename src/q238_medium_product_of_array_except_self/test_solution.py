""" Testing solution """

import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([0, 0], [0, 0]),
        ([1, 0], [0, 1]),
        ([-1, 1], [1, -1]),
        ([-2, -3], [-3, -2]),
    ],
)
def test_solution(nums, expected):
    """
    Checking Test Cases
    """
    assert Solution().productExceptSelf(nums) == expected
