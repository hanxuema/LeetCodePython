#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.74%)
# Likes:    1377
# Dislikes: 99
# Total Accepted:    386.7K
# Total Submissions: 845.6K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = float("inf")
        for i, a in enumerate(nums):
            left,right = i+1,len(nums)-1
            while left < right:
                b = nums[left]
                c = nums[right]
                sum = a + b + c
                if sum == target:
                    return sum
                if abs(sum-target) < abs(res-target):
                    res = sum
                if sum < target:
                    left += 1
                if sum > target:
                    right -= 1
        return res
     # @lc code=end

