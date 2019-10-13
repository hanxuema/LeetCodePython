#
# @lc app=leetcode id=292 lang=python
#
# [292] Nim Game
#

# @lc code=start
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if i have 1,2,3 ok
        # if i have 4 not ok
        # if i have 5, i choose 1
        return n % 4 != 0
# @lc code=end

