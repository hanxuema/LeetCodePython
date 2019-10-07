#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        if n == 2:
            return 2
        res = [1, 2]
        for i in range(2,n,1) :
            val = res[i - 1] + res[i - 2]
            res.append(val)
        return res[len(res) - 1]

# s = Solution()
# print(s.climbStairs(5))