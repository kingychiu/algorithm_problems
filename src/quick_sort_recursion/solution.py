"""
    <problem link>
"""


class Solution:
    # pylint: disable=too-few-public-methods
    """
    Solution
    """

    def _partition(self, start, end, arr):
        pivot = start
        while True:
            # keep looking for a value > the pivot
            # from the left
            while start <= end and arr[start] <= arr[pivot]:
                start += 1

            # keep looking for a value <= the pivot
            # from the right
            while start <= end and arr[end] > arr[pivot]:
                end -= 1
            
            if start < end:  # swap
                arr[start], arr[end] = arr[end], arr[start]
            else:
                break
        # move the pivot to the correct location.
        arr[end], arr[pivot] = arr[pivot], arr[end]
        # return the new location of the pivot value.
        return end

    def _sort(self, start, end, arr):
        # only sort when there are 2 or more items
        if start < end:
            # partition
            pivot = self._partition(start, end, arr)
            # recursive call
            self._sort(start, pivot - 1, arr)
            self._sort(pivot + 1, end, arr)

    def get_submission(self, arr):
        # pylint: disable=no-self-use
        """
        Quick Sort
        """
        self._sort(0, len(arr) - 1, arr)
        return arr
