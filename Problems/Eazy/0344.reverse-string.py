#
# @lc app=leetcode id=344 lang=python
#
# [344] Reverse String
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            # s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
# @lc code=end

