#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isPos = x > 0
        res = 0
        a = abs(x)
        while a != 0:
            lastDigit = a % 10
            res = res * 10 + lastDigit
            a = a // 10 # remove last digit
        if not isPos:
            res = 0 - res
        if res >  2 ** 31 or res < -(2 ** 31 -1):
            return 0
        return res


