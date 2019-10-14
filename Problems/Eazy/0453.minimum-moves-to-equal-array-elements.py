#
# @lc app=leetcode id=453 lang=python
#
# [453] Minimum Moves to Equal Array Elements
#
import unittest
# @lc code=start
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        target = min(nums)
        for num in nums:
            res += num - target
        return res
        
# @lc code=end

class TestStringMethods(unittest.TestCase):
       
    def test1and2(self):
        s = Solution()
        self.assertEqual(s.minMoves([1,2,3]),3)
        # self.assertEqual(s.arrangeCoins(2),1)
    
#     def test345(self):
#         s = Solution()
#         self.assertEqual(s.arrangeCoins(3),2)
#         self.assertEqual(s.arrangeCoins(4),2)
#         self.assertEqual(s.arrangeCoins(5),2)



if __name__ == '__main__':
    unittest.main() 
# print(s.arrangeCoins(8))