""" Testing solution """

import pytest
from src.maximum_number_of_visible_points.solution import Solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([[], 90, [1, 1]], 0),
        ([[[2, 1], [2, 2], [3, 3]], 90, [1, 1]], 3),
        ([[[2, 1], [2, 2], [3, 4], [1, 1]], 90, [1, 1]], 4),
        ([[[1, 0], [2, 1]], 13, [1, 1]], 1),
        ([
            [[1, 1], [2, 2], [1, 2], [2, 1]],
            0,
            [1, 1],
        ], 2),
        ([
            [[1, 1], [2, 2], [3, 3], [4, 4], [1, 2], [2, 1]],
            0,
            [1, 1]
        ], 4),
        ([
            [[45, 26], [82, 12], [33, 83], [58, 50], [55, 92], [66, 42], [25, 74], [74, 74], [36, 87], [7, 41], [89, 36], [
                44, 22], [84, 9], [96, 90], [75, 51], [87, 15], [50, 75], [90, 84], [56, 18], [43, 48], [23, 27], [100, 34]],
            12,
            [32, 37],
        ], 4),
        ([
            [[60, 61], [58, 47], [17, 26], [87, 97], [63, 63], [26, 50], [70, 21], [3, 89], [51, 24], [55, 14], [6, 51], [
                64, 21], [66, 33], [54, 35], [87, 38], [30, 0], [37, 92], [92, 12], [60, 73], [75, 98], [1, 11], [88, 24], [82, 92]],
            44,
            [15, 50],
        ], 11),
        ([
            [[70, 66], [97, 39], [79, 45], [74, 40], [27, 31], [62, 79], [77, 13], [93, 97], [67, 1], [99, 40], [12, 50], [57, 5], [87, 15], [24, 33], [44, 98], [7, 28], [40, 94], [36, 29], [51, 28], [38, 93], [54, 88], [53, 71], [98, 99], [3, 13], [90, 38], [22, 92], [30, 10], [30, 43], [54, 50], [65, 89], [57, 23], [43, 10], [47, 2], [76, 0], [90, 95], [5, 77], [9, 49], [79, 38], [77, 68], [26, 52], [97, 1], [35, 40], [60, 76], [77, 19], [21, 33], [94, 83], [64, 29], [3, 26], [36, 83], [16, 74], [17, 94], [69, 3], [95, 98], [44, 81], [65, 99], [21, 19], [99, 91], [96, 41], [48, 0], [28, 28], [70, 93], [80, 12], [15, 40], [28, 60], [42, 19], [25, 77], [34, 57], [24, 30], [83, 40], [81, 42], [80, 76], [74, 48], [66, 66], [98, 84], [48, 52], [90, 63], [6, 29], [16, 17], [64, 93], [83, 26], [93, 2], [14, 97], [87, 38], [87, 51], [14, 23], [3, 56], [48, 3], [71, 33], [
                63, 70], [46, 73], [97, 23], [60, 60], [98, 56], [92, 92], [73, 38], [6, 23], [70, 82], [33, 70], [29, 71], [3, 29], [61, 31], [11, 37], [91, 8], [28, 93], [21, 18], [73, 32], [21, 36], [11, 10], [79, 85], [57, 44], [19, 47], [26, 71], [58, 73], [16, 91], [1, 10], [83, 88], [36, 65], [42, 20], [21, 57], [6, 4], [68, 44], [66, 99], [51, 77], [29, 9], [78, 6], [15, 69], [86, 63], [91, 32], [65, 23], [87, 63], [55, 61], [25, 12], [4, 96], [10, 86], [72, 74], [36, 71], [56, 70], [6, 24], [13, 52], [90, 21], [60, 18], [85, 47], [11, 36], [73, 29], [21, 9], [66, 87], [92, 98], [40, 31], [45, 81], [8, 21], [33, 71], [6, 9], [31, 29], [61, 70], [86, 18], [82, 29], [68, 94], [97, 98], [53, 50], [71, 22], [71, 4], [36, 45], [38, 28], [32, 37], [52, 49], [91, 43], [79, 79], [84, 81], [64, 47], [23, 48], [72, 49], [78, 61], [34, 48], [83, 39], [32, 36], [18, 27], [91, 72]],
            86,
            [43, 45],
        ], 67)
    ],
)
def test_solution(test_input, expected):
    """
        Checking Test Cases
    """
    assert Solution().visible_points(*test_input) == expected
