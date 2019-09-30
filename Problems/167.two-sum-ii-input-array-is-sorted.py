#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) < 2:
            return []

        left, right = 0, len(numbers) -1
        while left < right:
            sum =  numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left+1, right+1]
# @lc code=end

