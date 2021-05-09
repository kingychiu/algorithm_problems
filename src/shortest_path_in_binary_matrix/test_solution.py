""" Testing solution """

import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([], 0),
        ([[0, 1], [1, 0]], 2),
        ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
        ([[0, 1], [1, 1]], -1),
        ([[0]], 1),
        ([[1]], -1),
    ],
)
def test_solution(test_input, expected):
    """
    Checking Test Cases
    """
    assert Solution().get_submission(test_input) == expected
