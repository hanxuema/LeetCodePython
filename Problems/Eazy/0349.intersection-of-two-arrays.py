#
# @lc app=leetcode id=349 lang=python
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        set1 = set()
        set2 = set()
        for n in nums1:
            set1.add(n)
        for n in nums2:
            if n in set1:
                set2.add(n)
        return set2
# @lc code=end

