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
        # check if minus number
        isMinus = x < 0
        # convert x from int to string
        # loop from end to begin
        res = int(str(abs(x))[::-1])
        if res > 2 ** 31 -1 or res <  -2 ** 31:
            return 0
        if isMinus:
            return 0 - res
        else:
            return res


