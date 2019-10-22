# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # if the array has less than 2 items, return empty array
        if len(nums) < 2:
           return []

        # setup a dictionary, lookup in python key-value pair
        lookup = {}
        # for loop the nums array,  
        for idx, item in enumerate(nums):
        # i wil be 0,1,2,3  item will be 2, 7 ,11, 15
            if (target - item) in lookup:
                # return the index 
                return [idx, lookup[target - item]]
                # if target - num not in the dic, add it, it will be <2,1> item 2 has index of 1
            lookup[item] = idx
        return []

nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum(nums, target))
