#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (43.97%)
# Likes:    1133
# Dislikes: 51
# Total Accepted:    258.2K
# Total Submissions: 587.2K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        if candidates is None or len(candidates) == 0:
            return res
        self.dfs(candidates, target, res, 0, [])
        return res

    def dfs(self, candidates, target, res, index, subset):
        subset.sort()
        if sum(subset) > target:
            return
        if sum(subset) == target:
            if subset not in res:
                res.append(subset)
            return 
        for i in range(index, len(candidates)):
            ss = subset + [candidates[i]]
            self.dfs(candidates, target, res, i+1, ss)
        
# @lc code=end

