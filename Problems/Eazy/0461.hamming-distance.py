#
# @lc app=leetcode id=461 lang=python
#
# [461] Hamming Distance
#

# @lc code=start
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        t = x ^ y
        res = 0
        while t > 0:
            res += t % 2
            t = t // 2
        return res
# @lc code=end

