#
# @lc app=leetcode id=108 lang=python
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (52.77%)
# Likes:    1420
# Dislikes: 150
# Total Accepted:    299.6K
# Total Submissions: 567.6K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted array: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def toBst(nums, start, end):
            if start > end:
                return None
            mid = (start + end ) // 2
            node = TreeNode(nums[mid])
            node.left =  toBst(nums, start, mid -1)
            node.right = toBst(nums, mid + 1, end)
            return node
        return toBst(nums, 0, len(nums) -1)
            
if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    Solution().sortedArrayToBST(nums)
