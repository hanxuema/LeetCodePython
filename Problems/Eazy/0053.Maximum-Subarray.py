class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        localMax, globalMax = 0,0
        for num in nums:
            localMax = max(0, localMax + num)
            globalMax = max(globalMax, localMax)
        return globalMax


s= Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))