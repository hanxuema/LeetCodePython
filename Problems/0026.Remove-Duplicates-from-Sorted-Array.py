class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [0,0,1,1,1,2,2,3,3,4],
        # [0,1,2,3,4]

        count = 0
        for i in range(len(nums)):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]
        return count + 1


        