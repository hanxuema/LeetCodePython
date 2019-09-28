# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isPos = x > 0
        res = 0
        a = abs(x)
        while(a != 0):
            temp = a % 10
            res = res * 10 + temp
            a = a // 10
        if isPos == False:
            res = 0 - res
        if res > 2 ** 31 -1 or res < -(2 **31):
            return 0
        return res


s = Solution()
print(s.reverse(120))
print(s.reverse(123))
print(s.reverse(-876))
