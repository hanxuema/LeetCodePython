#
# @lc app=leetcode id=441 lang=python
#
# [441] Arranging Coins
#
# https://leetcode.com/problems/arranging-coins/description/
#
# algorithms
# Easy (38.75%)
# Likes:    228
# Dislikes: 508
# Total Accepted:    79.5K
# Total Submissions: 205.1K
# Testcase Example:  '5'
#
# You have a total of n coins that you want to form in a staircase shape, where
# every k-th row must have exactly k coins.
# ⁠
# Given n, find the total number of full staircase rows that can be formed.
# 
# n is a non-negative integer and fits within the range of a 32-bit signed
# integer.
# 
# Example 1:
# 
# n = 5
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# 
# Because the 3rd row is incomplete, we return 2.
# 
# 
# 
# Example 2:
# 
# n = 8
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
# 
# Because the 4th row is incomplete, we return 3.
# 
# 
#
import unittest
# @lc code=start
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
      
        left, right = 0, n
        while left <= right:
            mid = (right + left) //2
            sums = mid * (mid + 1) // 2
            if sums == n:
                return mid
            elif sums > n:
                right = mid-1
            else:
                left = mid +1
        return right 

# @lc code=end

# class TestStringMethods(unittest.TestCase):
       
#     def test1and2(self):
#         s = Solution()
#         self.assertEqual(s.arrangeCoins(1),1)
#         self.assertEqual(s.arrangeCoins(2),1)
    
#     def test345(self):
#         s = Solution()
#         self.assertEqual(s.arrangeCoins(3),2)
#         self.assertEqual(s.arrangeCoins(4),2)
#         self.assertEqual(s.arrangeCoins(5),2)



if __name__ == '__main__':
    # print(8 * 3)
    unittest.main() 
# print(s.arrangeCoins(8))


