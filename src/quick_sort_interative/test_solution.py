""" Testing solution """

import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "test_input",
    [
        [2, 1, 3],
        [10, 80, 30, 90, 40, 50, 70],
    ],
)
def test_solution(test_input):
    """
    Checking Test Cases
    """
    assert Solution().get_submission(test_input) == sorted(test_input)
