"""
    https://leetcode.com/problems/minimum-window-substring/
"""
from typing import List, Tuple, Optional

import math
from src.data_structures.leetcode.tree import Node


class Solution:
    # pylint: disable=too-few-public-methods
    """
        Solution
    """

    def min_window(self, s: str, t: str) -> str:
        # pylint: disable=no-self-use
        """
            Return the minimum window in s which will contain all the characters in t.
            If there is no such window in s that covers all characters in t, return the empty string "".
        """
        s_length = len(s)
        missing_count = len(t)
        missing_dict = {c: 0 for c in t}
        for c in t:
            missing_dict[c] += 1

        init_start = 0
        init_end = 0

        min_length = float("+inf")
        min_str = ""
        while init_end < s_length:
            start = init_start
            end = init_end

            valid_range = False
            # Find a range from 0 to end
            for end in range(init_end, s_length):
                # If the charather is in the t string
                if s[end] in missing_dict:
                    # Update the missing counters
                    missing_dict[s[end]] -= 1
                    # If it is a necessary match (E.g.: not the 3rd "A" for t string "AAB")
                    if missing_dict[s[end]] >= 0:
                        # Only update the missing_count for a necessary new char
                        missing_count -= 1
                
                # Found a valid window
                if missing_count == 0:
                    valid_range = True
                    break

            # If there is no valid window found, the search is done.
            # It is because the above loop will end at the last idx of the s string.
            if not valid_range:
                break

            # If we found a valid window, we optimize it by moving the start pointer forward.
            # Find a range from start to end
            for start in range(init_start, end+1):
                # try to pop start idx to see
                if s[start] in missing_dict:
                    if missing_dict[s[start]] == 0:
                        # The start cannot be removed.
                        break
                    missing_dict[s[start]] += 1

            this_length = end - start + 1
            if this_length <= min_length:
                min_length = this_length
                min_str = s[start: end+1]

            # Slide forward to find other possible windows
            if s[start] in missing_dict:
                # Moving the start pointer requires us to the states.
                missing_dict[s[start]] += 1
                missing_count += 1

            init_end = end + 1
            init_start = start + 1

        return min_str
