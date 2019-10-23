#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self,n):
        res = []
        if n <= 0:
            return res
        left,right,subset = n,n,""
        self.dfs(res, left, right, subset)
        return res

    def dfs(self, res, left, right, subset):
        if left > right:
            return
        if left == 0 and right == 0:
            res.append(subset)
            return
        if left > 0 :
            self.dfs(res, left-1, right, subset+"(")
        if right > 0:
            self.dfs(res, left, right-1, subset+")")

s = Solution()
s.generateParenthesis(3)
# @lc code=end

