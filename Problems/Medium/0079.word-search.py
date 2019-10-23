#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#

# @lc code=start
class Solution(object):
    def exist(self, board, word):
        if len(word) == 0:
            return True
        if board is None or len(board) == 0 or len(board[0]) == 0 :
            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.dfs(board,row,col,0,word):
                        return True
        return False
    
    def dfs(self,board,row,col,index,word):
        if index == len(word):
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[index]:
            return False
        board[row][col] = "."
        res = self.dfs(board,row,col+1,index+1,word) or self.dfs(board,row,col-1,index+1,word) or self.dfs(board,row+1,col,index+1,word) or self.dfs(board,row-1,col,index+1,word)
        board[row][col] = word[index]

        return res
        
# @lc code=end
s = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word ="ABCCED"
print(s.exist(board,word))
