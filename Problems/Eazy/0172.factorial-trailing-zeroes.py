#
# @lc app=leetcode id=172 lang=python
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n != 0:
            result = result + n // 5
            n = n // 5
        return result

# if __name__ == "__main__":
#     print(Solution().trailingZeroes(26))
# @lc code=end

