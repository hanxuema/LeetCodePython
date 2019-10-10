#
# @lc app=leetcode id=162 lang=python
#
# [162] Find Peak Element
#

# @lc code=start
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        for i in range(len(nums) -1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums) - 1
# @lc code=end

