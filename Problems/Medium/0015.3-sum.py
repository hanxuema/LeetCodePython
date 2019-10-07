#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return []
        # [-1, 0, 1, 2, -1, -4],
        nums.sort()
        # [-4,-1,-1,0,1,2,],
        res = []
        for i,a in enumerate(nums):
            if i >= 1 and nums[i-1] == a:
                continue
            left,right = i + 1, len(nums) - 1
            while left < right:
                b = nums[left]
                c = nums[right]
                sum = a + b + c
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    res.append([a,b,c])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -=1
        return res

# @lc code=end

