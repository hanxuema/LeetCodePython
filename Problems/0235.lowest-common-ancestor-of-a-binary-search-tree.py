#
# @lc app=leetcode id=235 lang=python
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or p is None or q is None:
            return None
        if min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q )
        elif max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
# @lc code=end

