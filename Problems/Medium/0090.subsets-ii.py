#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (44.05%)
# Likes:    1123
# Dislikes: 54
# Total Accepted:    229.5K
# Total Submissions: 520.9K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums): 
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []
        res = []
        self.dfs(nums, res, 0, [])
        return res
    
    def dfs(self, nums, res, index, subset):
        subset.sort()
        if subset not in res:
            res.append(subset)
        for i in range(index, len(nums)):
            s = subset + [nums[i]]
            self.dfs(nums,res,i+1,s)
            
        
# @lc code=end
s = Solution()
print(s.subsetsWithDup([4,4,4,1,4]))

