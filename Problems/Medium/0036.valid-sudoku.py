#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start


class Solution(object):
    # https://www.youtube.com/watch?v=4-SF0-p98NM
    # difficult to understand
    def isValidSudoku(self, board):
        s = set()
        s.add((1,3))
        for row in range(len(board)):
            rows = set()
            cols = set()
            cubes = set()
            for col in range(len(board[row])): 
                if board[row][col] != "." and  board[row][col] in rows:
                    print("{} {} {} row, col board[row][col]".format(row, col, board[row][col]))
                    return False
                else:
                    rows.add(board[row][col])
                print("{} rows".format(rows))

                if board[col][row] != "." and board[col][row] in cols:
                    print("{} {} {} col, row board[col][row]".format(col, row, board[col][row]))
                    return False
                else:
                    cols.add(board[col][row])
                print("{} cols".format(cols))
                rowIndex = 3 * (row // 3)
                colIndex = 3 * (row % 3)
                board1 = rowIndex + col // 3
                board2 = colIndex + col % 3
                print("{} {} {} board1, board2 board[board1][board2]".format(board1, board2, board[board1][board2]))

                if board[board1][board2] != "." and board[board1][board2] in cubes:
                    print("{} cubes".format(cubes))
                    return False
                else:
                    cubes.add(board[board1][board2])
        return True

    def printBoard(self, board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                val = board[row][col]
                print("{} {} {}".format(row, col, val))

# @lc code=end


s = Solution()
# board = [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(s.isValidSudoku(board))
