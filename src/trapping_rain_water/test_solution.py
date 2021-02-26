""" Testing solution """

import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([], 0),
        ([0, 1, 0], 0),
        ([1], 0),
        ([1, 0], 0),
        ([0, 1], 0),
        ([1, 0, 0], 0),
        ([1, 0], 0),
        ([2, 0, 3], 2),
        ([3, 0, 2], 2),
        ([10, 0, 1], 1),
        ([10, 0, 2], 2),
        ([2, 0, 3], 2),
        ([2, 0, 10], 2),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
    ],
)
def test_solution(test_input, expected):
    """
        Checking Test Cases
    """
    assert Solution().trap(test_input) == expected
