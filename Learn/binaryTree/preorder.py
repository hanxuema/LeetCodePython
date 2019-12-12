# Given a binary tree, return the preorder traversal of its nodes' values

# preorder traversals NLR node, then left, then right

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,2,3]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import unittest
class Solution(object):
    def preorderTraversal(self, root):
        res = []
        self.dfs(root, res)
        return res
    
    def dfs(self, root, res):
        if root is None:
            return
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        return res
        
input = [1,None,2,3]
s = Solution()
res = s.preorderTraversal(input)
print("test {} is {}".format("e", (res == [1,2,3])))