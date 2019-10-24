#
# @lc app=leetcode id=51 lang=python
#
# [51] N-Queens
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        if n <= 0 :
            return self.res
        self.cols, self.diff, self.same = set(),set(),set()
        board = []
        for i in range(n):
            temp =[]
            for j in range(n):
                temp.append(".")
            board.append(temp)
        self.dfs(n,0,board)
        return self.res
    
    def dfs(self,n,row, board):
        if row == n:
            temp = []
            for i in range(len(board)):
                rowst = ""
                for j in range(len(board[i])):
                    rowst += board[i][j]
                temp.append(rowst)
            self.res.append(temp)
         
        
        for i in range(n):
            if i in self.cols or (row-i) in self.diff or (row+i) in self.same:
                continue

            self.cols.add(i)
            self.diff.add(row-i)
            self.same.add(row+i)
            board[row][i] = "Q"
            self.dfs(n,row+1,board)
            board[row][i] = "."
            self.cols.remove(i)
            self.diff.remove(row-i)
            self.same.remove(row+i)
        
# @lc code=end

s = Solution()
print(s.solveNQueens(4))