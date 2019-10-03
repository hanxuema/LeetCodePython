#
# @lc app=leetcode id=204 lang=python
#
# [204] Count Primes
#

# @lc code=start
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [None] * n
        nums[0] = False
        nums[1] = False
        for i in range(n):
            if nums[i] == None:
                nums[i] = True
                
                for j in range(2 * i, n, i):
                    nums[j] = False
        return sum(nums)

# @lc code=end

