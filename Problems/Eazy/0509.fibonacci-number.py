#
# @lc app=leetcode id=509 lang=python
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1 or N == 2:
            return 1
        return self.fib(N-1) + self.fib(N-2)

        res = [0] * (N+1)
        for i in range(N+1):
            if i == 0:
                res[i] = 0
            if i == 1 or i == 2:
                res[i] = 1
            if i > 2:
                res[i] = res[i-1] + res[i-2]
        return res[N]


# @lc code=end
s = Solution()
s.fib(8)
