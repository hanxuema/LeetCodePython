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
        while num >= 10:
            temp = num % 10 
            num = num // 10
            num = num + temp
        return num

# Solution().addDigits(38)
# @lc code=end

