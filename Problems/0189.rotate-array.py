#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:k], nums[k:] = nums[len(nums) -k:], nums[:len(nums) -k]
        # for i in range(len(nums)):
        #    temp =  nums[i]
        #    nums[i] = nums[len(nums)-k + i] 
        #    nums[len(nums) -k + i] = temp


# @lc code=end

