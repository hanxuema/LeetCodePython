#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        if nums is None or len(nums) == 0:
            return []
        res = []
        self.dfs(nums, res, [])
        return res
    
    def dfs(self, nums, res, subset):
        if len(nums) == len(subset):
            res.append(subset)
            return
        for i in range(len(nums)):
            if nums[i] in subset:
                continue
            ss = subset + [nums[i]]
            self.dfs(nums,res,ss)

# s = Solution()
# s.permute([1,2,3])
# @lc code=end
s = Solution()
print(s.permute([1,2,3]))
