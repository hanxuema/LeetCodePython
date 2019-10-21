#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (55.77%)
# Likes:    2463
# Dislikes: 59
# Total Accepted:    431.6K
# Total Submissions: 773.9K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        res  = []
        self.dfs(res, nums, 0, [])
        return res

    def dfs(self, res, nums, index, subset):
        res.append(subset[:])
        for i in range(index, len(nums)):
            ss = subset + [nums[i]]
            self.dfs(res, nums, i+1, ss)

        
# @lc code=end

