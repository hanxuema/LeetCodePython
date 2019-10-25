#
# @lc app=leetcode id=52 lang=python
#

# @lc code=start
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        self.res = 0
        self.cols, self.diff, self.same = set(), set(), set()
        self.dfs(n, 0)
        return self.res
        
    def dfs(self, n , row):
        if row >= n:
            self.res += 1
            return
        for i in range(n):
            if i in self.cols or (row+i) in self.same or (row-i) in self.diff:
                continue
            self.cols.add(i)
            self.diff.add(row-i)
            self.same.add(row+i)
            self.dfs(n,row+1)
            self.cols.remove(i)
            self.diff.remove(row-i)
            self.same.remove(row+i)
        
# @lc code=end

s = Solution()
print(s.totalNQueens(4))