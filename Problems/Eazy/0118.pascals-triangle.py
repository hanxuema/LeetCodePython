#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (48.04%)
# Likes:    853
# Dislikes: 84
# Total Accepted:    289.6K
# Total Submissions: 602.9K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            cur =[]
            for j in range(i+1):
                if j in (0,i):
                    cur.append(1)
                else:
                    cur.append(result[i-1][j-1] + result[i-1][j])
            result.append(cur)
        return result



# if __name__ == '__main__':
#     print(Solution().generate(6))