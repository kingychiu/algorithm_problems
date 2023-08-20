""" Testing solution """

import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "candies,extra_candies,expected",
    [
        ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
        ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
        ([12, 1, 12], 10, [True, False, True]),
        ([1, 1], 1, [True, True])
    ],
)
def test_solution(candies, extra_candies, expected):
    """
    Checking Test Cases
    """
    assert Solution().kidsWithCandies(candies, extraCandies=extra_candies) == expected
