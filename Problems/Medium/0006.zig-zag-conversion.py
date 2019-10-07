#
# @lc app=leetcode id=6 lang=python
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s
        row, step =  0, 1
        res = ["" for r in range(numRows)]
        for c in s:
            res[row] += c
            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            row += step
        return "".join(res)

# s = Solution()
# s.convert("LEETCODEISHIRING",4)
 # @lc code=end

