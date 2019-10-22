#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) ==0 :
            return 0
        count = 0
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count + 1
# @lc code=end

print(Solution().removeDuplicates([0,0,1,1,2,2,3,3]))
# 0,0,1,1,2,2,3,3
# 0,1,1,1,2,2,3,3
# 0,1,1,1,2,2,3,3
# 0,1,2,1,2,2,3,3
# 0,1,2,3,2,2,3,3


