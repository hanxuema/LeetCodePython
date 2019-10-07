#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#

# @lc code=start


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pretwo, pre = 0, 0
        for n in nums:
            pretwo , pre = pre,max(pretwo + n, pre)
        return pre


# a,b = 1,4
# b,a = a,b
# print(str(a))
# print(str(b))

# if __name__ == '__main__':

#     print(Solution().rob([8, 4, 8, 5, 9, 6, 5, 4, 4, 10]))

# @lc code=end
