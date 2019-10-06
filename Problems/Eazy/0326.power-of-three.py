#
# @lc app=leetcode id=326 lang=python
#
# [326] Power of Three
#

# @lc code=start
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0 or n == 2:
            return False
        while n % 3 == 0:
            n = n // 3
        return n == 1
# @lc code=end

