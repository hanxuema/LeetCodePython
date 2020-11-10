#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (42.68%)
# Likes:    1317
# Dislikes: 46
# Total Accepted:    281.9K
# Total Submissions: 660.4K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if nums is None or len(nums) == 0:
            return res
        nums.sort()
        self.dfs(nums, res, [])
        return res
    
    def dfs(self, nums, res, subset):
        if len(nums) == len(subset) and subset not in res:
            res.append(subset)
            return
        for i in range(len(nums)):
            if nums[i] in subset:
                continue
            ss = subset + [nums[i]]
            self.dfs(nums,res, ss)
        
# @lc code=end

s = Solution()
print(s.permuteUnique([1,1,2]))[1,1,2]