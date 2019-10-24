#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    self.dfs(grid,row,col)
                    res += 1
        return res

    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
            return
        grid[row][col] = "0"
        self.dfs(grid, row+1, col)
        self.dfs(grid, row, col+1)
        self.dfs(grid, row-1, col)
        self.dfs(grid, row, col-1)

        
# @lc code=end

