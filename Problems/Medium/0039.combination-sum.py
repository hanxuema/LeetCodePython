#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (51.34%)
# Likes:    2570
# Dislikes: 78
# Total Accepted:    410.6K
# Total Submissions: 799.7K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
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
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target): 
        res = []
        self.dfs(candidates,target,0,res,[])
        return res
    
    def dfs(self, candidates, target, index, res, subset):
        if sum(subset) > target:
            return
        if sum(subset) == target:
            res.append(subset)
            return
        for i in range(index, len(candidates)):
            ss = subset + [candidates[i]]
            self.dfs(candidates, target,i,res, ss) # use i to reuse the existing elements, #use i + 1 to NOT include exising elements
        
        
# @lc code=end
s = Solution()
s.combinationSum([2,3,6,7],7)
