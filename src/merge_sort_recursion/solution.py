"""
    Merge Sort with recursion
"""


class Solution:
    # pylint: disable=too-few-public-methods
    """
    Solution
    """

    def _sort(self, arr):
        arr_length = len(arr)
        if arr_length == 1:
            return arr
        # get a mid point
        mid = arr_length // 2
        sorted_left = self._sort(arr[:mid])
        sorted_right = self._sort(arr[mid:])
        left_length = len(sorted_left)
        right_length = len(sorted_right)
        # merge
        result_ptr = left_ptr = right_ptr = 0
        while left_ptr < left_length and right_ptr < right_length:
            if sorted_left[left_ptr] <= sorted_right[right_ptr]:
                # pick left
                arr[result_ptr] = sorted_left[left_ptr]
                left_ptr += 1
            else:
                # pick right
                arr[result_ptr] = sorted_right[right_ptr]
                right_ptr += 1
            result_ptr += 1
        
        # clean up left
        while left_ptr < left_length:
            # pick left
            arr[result_ptr] = sorted_left[left_ptr]
            left_ptr += 1
            result_ptr += 1
        
        # clean up right
        while right_ptr < right_length:
            # pick right
            arr[result_ptr] = sorted_right[right_ptr]
            right_ptr += 1
            result_ptr += 1

        return arr

    def get_submission(self, arr):
        # pylint: disable=no-self-use
        """
        Merge Sort
        """
        self._sort(arr)
        return arr
