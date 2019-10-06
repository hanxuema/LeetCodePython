#
# @lc app=leetcode id=350 lang=python
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if len(nums1) == 0 or len(nums2) == 0:
            return []
        lookup = {}
        for n in nums1:
            if n in lookup:
                lookup[n] += 1
            else:
                lookup[n] = 1
        res = []
        for n in nums2:
            if n in lookup and lookup[n] > 0:
                res.append(n)
                lookup[n] -= 1
        return res
        
# @lc code=end

 