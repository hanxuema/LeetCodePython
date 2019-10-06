#
# @lc app=leetcode id=263 lang=python
#
# [263] Ugly Number
#

# @lc code=start
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for n in [2,3,5]:
            while num % n == 0:
                num = num // n
        return num == 1
        

# @lc code=end

