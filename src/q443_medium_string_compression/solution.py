#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#


# @lc code=start
class Solution:
    def compress(self, chars: list[str]) -> int:
        write_ptr = 0
        read_start_ptr = 0
        read_end_ptr = 0

        while True:
            if read_end_ptr == len(chars) or chars[read_start_ptr] != chars[read_end_ptr]:
                chars[write_ptr] = chars[read_start_ptr]
                count = read_end_ptr - read_start_ptr
                if count > 1:
                    count_str = str(count)
                    for ptr in range(0, len(count_str)):
                        chars[write_ptr + 1 + ptr] = count_str[ptr]
                    write_ptr += len(count_str) + 1
                else:
                    write_ptr += 1
                read_start_ptr = read_end_ptr
                
                if read_end_ptr == len(chars):
                    break
            else:
                read_end_ptr += 1

        return write_ptr


# @lc code=end
