#
# @lc app=leetcode id=437 lang=python
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.subSum(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    
    def subSum(self,root,sum):
        if not root:
            return 0
        count = 0
        if root.val == sum:
            count += 1
        
        count += self.subSum(root.left,sum-root.val)
        count += self.subSum(root.right, sum-root.val)
        return count
# @lc code=end

