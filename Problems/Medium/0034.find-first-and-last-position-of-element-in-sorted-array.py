#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#
import unittest
# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1,-1]
        if nums is None or len(nums) == 0:
            return res
        res[0] = self.findFirst(nums, target)
        res[1] = self.findLast(nums, target)

        return res
    
    def findFirst(self, nums, target):
        left, right = 0, len(nums) -1 
        index= -1
        while left <= right:
            mid = left + (right -left) //2
            if nums[mid] >= target:
                right = mid-1
            else:
                left = mid+1
            if nums[mid] == target:
                index = mid

        return index

    def findLast(self, nums, target):
        left,right, index = 0, len(nums) -1 , -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid+1
            else:
                right = mid-1
            if nums[mid] == target:
                index = mid

        return index
# @lc code=end

class teset(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertEqual(s.searchRange([5,7,7,8,8,10], 8),[3,4])

if __name__ == '__main__':
    # print(8 * 3)
    unittest.main()