#
# @lc app=leetcode id=476 lang=python
#
# [476] Number Complement
#
# https://leetcode.com/problems/number-complement/description/
#
# algorithms
# Easy (62.76%)
# Likes:    597
# Dislikes: 76
# Total Accepted:    116.3K
# Total Submissions: 185.3K
# Testcase Example:  '5'
#
# Given a positive integer, output its complement number. The complement
# strategy is to flip the bits of its binary representation.
# 
# Note:
# 
# The given integer is guaranteed to fit within the range of a 32-bit signed
# integer.
# You could assume no leading zero bit in the integer’s binary
# representation.
# 
# 
# 
# Example 1:
# 
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.
# 
# 
# 
# Example 2:
# 
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and
# its complement is 0. So you need to output 0.
# 
# 
#

import unittest
# @lc code=start
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = self.convertIntToBinary(num)
        temp = temp ^ temp

    def convertIntToBinary(self, num):
        res = 0
        while num > 0:
            temp = num % 2
            res = res * 10 + temp
            num = num // 2

        return res


# @lc code=end
 
class TestStringMethods(unittest.TestCase):

    def test1(self):
        s = Solution()
        s.findComplement(5)
        self.assertEqual(s.convertIntToBinary(5), 101)

if __name__ == "__main__":
    unittest.main()