#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#

# @lc code=start


class Solution(object):
    def permuteUnique(self, nums):
        res = []
        if nums is None or len(nums) == 0:
            return res
        nums.sort()
        visited = [False]*(len(nums))
        self.dfs(nums,res,visited,[])
        return res
    
    def dfs(self,nums,res,visited,subset):
        if len(nums) == len(subset):
            res.append(subset)
            return
        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            visited[i] = True
            ss = subset + [nums[i]]
            self.dfs(nums,res,visited,ss)
            visited[i] = False

# @lc code=end
s = Solution()
s.permuteUnique([1, 1, 2])
