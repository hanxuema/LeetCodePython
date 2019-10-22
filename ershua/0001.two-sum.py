#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # if len of nums is less than 2, no need to check
        if len(nums) < 2:
            return []
        # create a dictionary, key is num, value is the index of the num
        lookup = {}
        for i, num in enumerate(nums):
            if (target - num) in lookup:
                # if find a match, return current index and index of matched pair from lookup
                return [i, lookup[target - num]]
            lookup[num] = i
            
        return []
        

