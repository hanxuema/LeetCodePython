#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#	  def __init__(self, x):
#		  self.val = x
#		  self.left = None
#		  self.right = None

class Solution(object):
	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		
		def balanceRec(root):
			if root is None:
				return 0
			leftHeight = balanceRec(root.left)
			rightHeight = balanceRec(root.right)
			if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1 :
				return -1
			return max(leftHeight, rightHeight) + 1
		return balanceRec(root) >= 0

