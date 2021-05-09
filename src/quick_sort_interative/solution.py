"""
    Quick Sort with a queue/stack
"""


class Solution:
    # pylint: disable=too-few-public-methods
    """
    Solution
    """

    @staticmethod
    def _partition(start, end, arr):
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
            if start >= end:
                break
        # move the pivot to the correct location.
        arr[end], arr[pivot] = arr[pivot], arr[end]
        # return the new location of the pivot value.
        return end

    def get_submission(self, arr):
        # pylint: disable=no-self-use
        """
        Quick Sort
        """
        queue = [(0, len(arr) - 1)]
        while queue:
            start, end = queue.pop(0)
            if start < end:
                pivot = self._partition(start, end, arr)
                queue.append((start, pivot - 1))
                queue.append((pivot + 1, end))
        return arr
