#
# @lc app=leetcode id=463 lang=python
#
# [463] Island Perimeter
#

# @lc code=start
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) ==0:
            return 0
        res =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += 4
                    if i < len(grid) -1 and grid[i+1][j] == 1:
                        res -= 2
                    if j < len(grid[0]) -1 and grid[i][j+1] ==1:
                        res -= 2
        return res
# @lc code=end

