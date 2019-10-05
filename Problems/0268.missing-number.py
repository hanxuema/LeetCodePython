#
# @lc app=leetcode id=268 lang=python
#
# [268] Missing Number
#

# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        for n in range(len(nums) + 1):
            if n not in numset:
                return n 

# @lc code=end

