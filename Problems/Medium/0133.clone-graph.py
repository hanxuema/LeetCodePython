#
# @lc app=leetcode id=133 lang=python
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        visited = {}
        newNode = self.dfs(node,visited)
        return newNode
    
    def dfs(self,node,visited):
        if node is None:
            return None
        if node in visited:
            return visited[node]
        newNode = Node(node.val,[])
        visited[node] = newNode
        for n in node.neighbors:
            newNode.neighbors.append(self.dfs(n,visited))
        return newNode
# @lc code=end

s = Solution()
print(s.cloneGraph({"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}))