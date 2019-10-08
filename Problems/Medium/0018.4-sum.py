#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.nSum(sorted(nums),target, 4)
    
    def nSum(self, nums, target, n):
        if len(nums) < n or n < 2 or target > nums[-1] * n or target < nums[0] * n :
            return []
        res = []
        if n == 2:
            left, right = 0, len(nums) -1 
            while left <  right:
                sum = nums[left] + nums[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        for i in range(len(nums)):
            a = nums[i]
            fixedTarget = target - a
            if (nums[i] != nums[i-1] and i > 0) or i == 0:
                fixedResult = self.nSum(nums[i + 1:], fixedTarget, n -1)
                for result in fixedResult:
                    res.append([a] + result)
        return res
s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))
# @lc code=end

