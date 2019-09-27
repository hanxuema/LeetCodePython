#
# @lc app=leetcode id=119 lang=python
#
# [119] Pascal's Triangle II
#
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1] +[0] * rowIndex

        for i in range(rowIndex):
            result[0] = 1
            for j in range(i + 1, 0, -1):
                result[j] = result[j] + result[j-1]

        return result
if __name__ == '__main__':
    print(Solution().getRow(3))

