""" Testing solution """

import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "chars,expected",
    [
        (["a", "a", "b", "b", "c", "c", "c"], 6),
        (["a"], 1),
        (["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], 4),
        (["a", "a", "a", "b", "b", "a", "a"], 6),
    ],
)
def test_solution(chars, expected):
    """
    Checking Test Cases
    """
    assert Solution().compress(chars) == expected
