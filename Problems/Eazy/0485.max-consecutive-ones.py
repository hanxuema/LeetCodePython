#
# @lc app=leetcode id=485 lang=python
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        res = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
                res = max(res, count)
            else:
                count = 0

        return res
# @lc code=end
s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))

