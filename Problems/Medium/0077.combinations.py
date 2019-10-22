#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (50.33%)
# Likes:    977
# Dislikes: 56
# Total Accepted:    234.1K
# Total Submissions: 465.1K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        res = []
        self.dfs(n,res,1,[],k)
        return res


    def dfs(self, n, res, index, subset,k):
        if len(subset) == k:
            res.append(subset)
        for i in range(index, n+1):
            ss = subset + [i]
            self.dfs(n,res,i+1,ss,k)
        
# @lc code=end

