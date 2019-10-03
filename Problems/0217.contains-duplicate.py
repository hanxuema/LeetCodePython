#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        nums.sort()
        for i in range(len(nums) -1 ):
            if nums[i] == nums[i+1]:
                return True
        return False


         if len(nums) <= 1:
            return False
        lookup= {}
        for n in nums:
            if n in lookup:
                return True
            else:
                lookup[n] = True
# @lc code=end

