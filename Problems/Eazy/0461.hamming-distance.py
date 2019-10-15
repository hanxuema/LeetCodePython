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
        t = x^ y
        ans = 0
        while t > 0:
            # ans += t & 1
            # t = t >> 1
            ans += t % 2
            t = t // 2
        return ans     
# @lc code=end

