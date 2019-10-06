#
# @lc app=leetcode id=429 lang=python
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        cur = [root]
        next= []
        res = []

        while cur:
            temp = []
            for c in cur:
                temp.append(c.val)
                for n in c.children:
                    next.append(n)
            cur = next
            next = []
            res.append(temp)
        
        return res
                


# @lc code=end

