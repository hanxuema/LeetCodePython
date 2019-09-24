#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (62.15%)
# Likes:    1572
# Dislikes: 59
# Total Accepted:    586.7K
# Total Submissions: 944K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its depth = 3.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# if __name__ == '__main__':
#     root = TreeNode(3)
#     root.left= TrueeNode(9)
#     root.right = TrueeNode(20)
#     root.left.left= TrueeNode(9)
#     root.left.right= TrueeNode(9)
#     print(Solution().maxDepth(root))
