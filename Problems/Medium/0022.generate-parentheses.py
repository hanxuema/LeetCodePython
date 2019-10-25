#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self,n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        left,right,item = n,n,""
        self.helper(left, right, item, res)
        return res

    def helper(self, left, right, item, res):
        print("left {} right {} item {} res {}".format(left,right,item,res))
        if right < left:
            return 
        if left == 0 and right == 0:
            res.append(item)
        if left > 0:
            self.helper(left-1,right, item+"(", res)
        if right > 0:
            self.helper(left, right -1, item+")", res)
        
s = Solution()
s.generateParenthesis(3)
# @lc code=end

