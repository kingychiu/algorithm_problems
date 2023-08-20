""" Testing solution """

import pytest

from .solution import Solution
from .solution_optimal import Solution as OptimalSolution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 4, 5], True),
        ([5, 4, 3, 2, 1], False),
        ([2, 1, 5, 0, 4, 6], True),
        ([1], False),
        ([1, 2], False),
        ([1, 2, 3], True),
        ([1, 3, 2], False),
        ([1] * 5 * 10**5, False),
        ([1, 2, 3] * 5 * 10, True),
        ([20, 100, 10, 12, 5, 13], True),
        ([4, 6, 3, 4, 5], True),
        ([4, 10, 5, 1, 2, 3, -9, -7, -10], True),
    ],
)
def test_solution(nums, expected):
    """
    Checking Test Cases
    """
    assert Solution().increasingTriplet(nums) == expected
    assert OptimalSolution().increasingTriplet(nums) == expected
