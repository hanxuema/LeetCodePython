#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """ 
        while m  > 0 and n  > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m-1+n], nums1[m-1] = nums1[m-1], nums1[m-1+n] 
                m = m -1
            else:
                nums1[m-1+n] = nums2[n-1]
                n = n - 1
        if  m  == 0 and n > 0:
            nums1[:n] = nums2[:n]
            
        return nums1
 
        # while m > 0 and n > 0:
        #     if nums1[m-1] < nums2[n-1]:
        #         nums1[m-1+n] = nums2[n-1]
        #         n = n - 1
        #     else:
        #         nums1[m-1+n], nums1[m-1] = nums1[m-1], nums1[m-1+n]
        #         m = m -1
        # if m == 0 and n>0:
        #     nums1[:n] = nums2[:n]
        # return nums1

# if __name__ == "__main__":
#     nums1 = [2, 3, 5, 0, 0, 0, 0]
#     nums2 =          [1, 4, 6, 7]
#     print(Solution().merge(nums1, 3, nums2, 4))
