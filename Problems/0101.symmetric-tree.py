#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (44.46%)
# Likes:    2650
# Dislikes: 57
# Total Accepted:    464.8K
# Total Submissions: 1M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# But the following [1,2,2,null,3,null,3] is not:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if root is None:
			return True
		return self.isSymmetricRec(root.left, root.right)
		
	def isSymmetricRec(self,left, right):
		if left is None and right is None:
			return True
		if left is None or right is None or left.val != right.val:
			return False
		return self.isSymmetricRec(left.left, right.right) and self.isSymmetricRec(left.right, right.left)
        

 if __name__ == "__main__":
	root = TreeNode(1)
	root.left, root.right = TreeNode(2), TreeNode(2)
	root.left.left, root.right.right = TreeNode(3), TreeNode(3)
	root.left.right, root.right.left = TreeNode(4), TreeNode(4)
 	print(Solution().isSymmetric(root))