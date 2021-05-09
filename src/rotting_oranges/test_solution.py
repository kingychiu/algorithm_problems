""" Testing solution """
# pylint: disable=duplicate-code
import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([], 0),
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ([[0, 2]], 0),
    ],
)
def test_solution(test_input, expected):
    """
    Checking Test Cases
    """
    assert Solution().oranges_rotting(test_input) == expected
