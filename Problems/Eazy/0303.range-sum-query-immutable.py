#
# @lc app=leetcode id=303 lang=python
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.res = [0]
        for n in nums:
            self.res.append(n + self.res[-1])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.res[j+1] -self.res[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

