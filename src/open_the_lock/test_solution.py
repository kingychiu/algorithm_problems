""" Testing solution """

import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "deadends, target, expected",
    [
        (["0000"], "8888", -1),
        (["0201", "0101", "0102", "1212", "2002"], "0202", 6),
        (["8888"], "0009", 1),
        (["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888", -1)
    ],
)
def test_solution(deadends, target, expected):
    """
        Checking Test Cases
    """
    assert Solution().open_lock(deadends, target) == expected
