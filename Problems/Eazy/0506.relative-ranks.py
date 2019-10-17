#
# @lc app=leetcode id=506 lang=python
#
# [506] Relative Ranks
#

# @lc code=start
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return [] 
        temp =  sorted(nums,reverse=True) 
        lookup = {}
        for i in range(len(temp)):
            if i == 0:
                lookup[temp[i]] = "Gold Medal"
            if i == 1:
                lookup[temp[i]] = "Silver Medal"
            if i == 2:
                lookup[temp[i]] = "Bronze Medal"
            if i > 2:
                lookup[temp[i]] = str(i+1)
        res = []
        # {10:"Gold Medal", 3:"5", 8:"Bronze Medal", 9:"Silver Medal", 4: "4"}
        for i, n in enumerate(nums):
            res.append(lookup[n])
        return res
# @lc code=end
s = Solution()
print(s.findRelativeRanks([10,3,8,9,4]))
