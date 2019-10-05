#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        loc = 0
        for num in nums:
            if num != 0:
                nums[loc] = num
                loc += 1
        while loc < len(nums):
            nums[loc] = 0
            loc += 1

Solution().moveZeroes([0,1,0,3,12])
#       [0,1,0,3,12]
# first [1,3,12,3,12]
#       [1,3,12,0,0]
# @lc code=end

