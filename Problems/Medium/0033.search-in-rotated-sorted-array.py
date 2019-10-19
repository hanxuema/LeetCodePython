#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left < right: #find the smallest number in the array
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        start = left
        left = 0
        right = len(nums) -1 
        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start
        
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return -1
# @lc code=end

s = Solution()
print(s.search([3,1], 3))
