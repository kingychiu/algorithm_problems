""" Testing solution """

import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "times, N, K, expected",
    [
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 5, -1),
    ],
)
def test_solution(times, N, K, expected):
    """
    Checking Test Cases
    """
    assert Solution().get_submission(times, N, K) == expected
