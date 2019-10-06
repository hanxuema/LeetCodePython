#
# @lc app=leetcode id=414 lang=python
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findMaxNumberBelowMax(set, maxNumber):
            temp = min(set)
            for n in set:
                if n < maxNumber:
                    temp = max(temp, n)
            return temp

        set1 = set()
        for n in nums:
            set1.add(n)
        if len(set1) < 3:
            return max(set1)
        else:
            maxNumber = max(set1)
            temp = findMaxNumberBelowMax(set1, maxNumber) 
            res =  findMaxNumberBelowMax(set1, temp) 
            return res
# @lc code=end

