#
# @lc app=leetcode id=51 lang=python
#
# [51] N-Queens
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        self.res = []
        if n <= 0:
            return self.res
        self.cols, self.diff, self.same = set(),set(),set()
        temp =[]
        board1 = []
        for i in range(n):
            temp.append(".")
        for i in range(n):
            board1.append(temp)
        board = []
        for i in range(n):
            temp =[]
            for j in range(n):
                temp.append(".")
            board.append(temp)
        print("board1 {}".format(board1))
        self.dfs(n, 0, board1)
        print("res {}".format(self.res))

        print("board {}".format(board))
        self.res = []
        self.dfs(n, 0, board)
        print("res {}".format(self.res))
        
        return self.res
        
    def dfs(self, n, row, board):
        if row >= n :
            temp = []
            for i in range(len(board)):
                rowSt = ""
                for j in range(len(board[i])):
                    rowSt += board[i][j]
                temp.append(rowSt)
            self.res.append(temp)
            return
        for i in range(n):
            
            if i in self.cols or row + i in self.same or row - i in self.diff:
                continue
            self.cols.add(i)
            self.diff.add(row - i)
            self.same.add(row + i)
            board[row][i] = "Q"
            self.dfs(n, row+1, board)
            board[row][i] = "."
            self.cols.remove(i)
            self.same.remove(row + i)
            self.diff.remove(row - i)
        
# @lc code=end

s = Solution()
print(s.solveNQueens(4))