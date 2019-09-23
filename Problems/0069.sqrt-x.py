#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 4 :
            return 1
        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left ) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return left -1

 