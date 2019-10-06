#
# @lc app=leetcode id=404 lang=python
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def isLeaf(root):
            if root is None:
                return False
            if root.left or root.right:
                return False
            return True

        if root is None:
            return 0

        res = 0
        if isLeaf(root.left):
            res += root.left.val
        else:
            res += self.sumOfLeftLeaves(root.left)
        
        if root.right:
            res += self.sumOfLeftLeaves(root.right)

        return res 

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# s = Solution()
# s.sumOfLeftLeaves(root)
# @lc code=end

