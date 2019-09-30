#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, cnt = 0, 1

        for i in range(1, len(nums)):
            print ('nums[idx], cnt', nums[idx], cnt)
            if nums[idx] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    idx = i
                    cnt = 1

        return nums[idx]

# if __name__ == "__main__":
#     #print(Solution().majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]))
#     #print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
#     print(Solution().majorityElement([1, 2, 3, 4, 6,5, 5, 5, 5, 5,  5]))
# @lc code=end

