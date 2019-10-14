#
# @lc app=leetcode id=448 lang=python
#
# [448] Find All Numbers Disappeared in an Array
#
import unittest
# @lc code=start
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            index = abs(num) - 1
            nums[index] = 0 - abs(nums[index])
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        return res


# @lc code=end
# class TestStringMethods(unittest.TestCase):
       
#     def Test1(self):
#         s = Solution()
#         self.assertEqual(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]),[5,6]) 
        
# if __name__ == '__main__':
#     # print(8 * 3)
#     unittest.main() 

