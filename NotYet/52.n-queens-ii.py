#
# @lc app=leetcode id=52 lang=python
#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (54.15%)
# Likes:    339
# Dislikes: 129
# Total Accepted:    111.9K
# Total Submissions: 206.4K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# 
# 
# 
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
# 
# Example:
# 
# 
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown
# below.
# [
# [".Q..",  // Solution 1
# "...Q",
# "Q...",
# "..Q."],
# 
# ["..Q.",  // Solution 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    def totalNQueens(self, n):
        if n == 0:
            return 0
        self.cols = set()
        self.diff = set() # sum is the same value
        self.sum = set() # minus is the same value
        self.res = 0
        self.dfs(n,0)
        return self.res
    
    def dfs(self,n,row):
        if row >= n:
            self.res += 1
            return
        for i in range(n):
            if i not in self.cols and row - i not in self.diff and row + i not in self.sum:
                self.cols.add(i)
                self.diff.add(row-i)
                self.sum.add(row+i)
                print("row {}, i {}".format(row, i ))
                print("cols {}, dif {}, sum {}".format(self.cols, self.diff, self.sum))
                self.dfs(n,row+1)
                self.cols.remove(i)
                self.diff.remove(row-i)
                self.sum.remove(row+i)
                print("after remove cols {}, dif {}, sum {}, res {}".format(self.cols, self.diff, self.sum, self.res))
            else:
                print("alreay in row {} i {}".format(row, i))
                print("i {} cols {}".format(i, self.cols))
                print("row - i {} diff {}".format(row - i, self.diff))
                print("row + i {} sum {}".format(row + i, self.sum))
# @lc code=end
s = Solution()
print(s.totalNQueens(5))