#
# @lc app=leetcode id=29 lang=python
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend  >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = 0-res
        return min(max(-2147483648, res), 2147483647)
# @lc code=end

s = Solution()
print(s.divide(-283048234,79789))