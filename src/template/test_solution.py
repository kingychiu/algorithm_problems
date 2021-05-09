""" Testing solution """

import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "test_input,expected",
    [(1, 1)],
)
def test_solution(test_input, expected):
    """
    Checking Test Cases
    """
    assert Solution().get_submission(test_input) == expected
