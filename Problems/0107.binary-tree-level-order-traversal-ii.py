#
# @lc app=leetcode id=107 lang=python
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (48.33%)
# Likes:    847
# Dislikes: 162
# Total Accepted:    250K
# Total Submissions: 517.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        current = [root]
        while current:
            nextLevel = []
            val = []
            for node in current:
                if node.left is not None:
                    nextLevel.append(node.left)
                if node.right is not None:
                    nextLevel.append(node.right)
                val.append(node.val)
            current = nextLevel
            res.append(val)
        return res[::-1]
        

# if __name__ == '__main__':
#     root = TreeNode(3)
#     root.left = TreeNode(9)
#     root.right = TreeNode(20)
#     root.left.left = TreeNode(7)
#     root.left.right = TreeNode(15)
#     print(Solution().levelOrderBottom(root))
