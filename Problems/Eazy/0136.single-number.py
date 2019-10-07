#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            res ^= n
        return res
        # a ^ 0 = a
        # a ^ a = 0
        #[a,a,b,c,b]
        # 
