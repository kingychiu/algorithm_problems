#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    def check_divisible(self, s: str, d: str):
        times = len(s) // len(d)
        return s == d * times

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        
        # The gcd candidates start with the shortest string
        gcd = str1 if len1 < len2 else str2
        gcd_len = len(gcd)
        
        while gcd_len > 0:
            # Check if the candidate is a common divisor of str1 and str2
            if self.check_divisible(str1, gcd) and self.check_divisible(str2, gcd):
                return gcd
            
            # Update next by removing a char
            gcd_len -= 1
            gcd = gcd[:gcd_len]

        return ""
# @lc code=end
