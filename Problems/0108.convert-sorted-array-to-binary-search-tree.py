#
# @lc app=leetcode id=108 lang=python
#
# [108] Convert Sorted Array to Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def toBst(nums, left, right):
            if left > right:
                return None

            mid = (left + right )/2
            node = TreeNode(nums[mid])
            node.left = toBst(nums, left, mid -1)
            node.right = toBst(nums, mid + 1, right)
            return node
        return toBst(nums, 0, len(nums) -1)

