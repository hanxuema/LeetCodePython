#
# @lc app=leetcode id=258 lang=python
#
# [258] Add Digits
#

# @lc code=start
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """ 
        if num <= 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9

# Solution().addDigits(38)
# @lc code=end

