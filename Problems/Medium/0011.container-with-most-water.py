#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 2:
            return min(height[0], height[1])
        res = 0
        left, right = 0, len(height) - 1
        while left < right:
            minHeight = min(height[left], height[right])
            res = max(res, minHeight * (right - left))
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return res
# @lc code=end

