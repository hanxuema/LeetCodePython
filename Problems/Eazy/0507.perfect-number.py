#
# @lc app=leetcode id=507 lang=python
#
# [507] Perfect Number
#
import math
# @lc code=start
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        i = int(math.sqrt(num))
        res = 1
        for k in range(2,i+1):
            if num % k == 0:
                res += k + num // k
        return res == num
# @lc code=end
s = Solution()
print(s.checkPerfectNumber(28))
