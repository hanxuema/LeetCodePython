#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        # pointer is the lower index of a non repeating sub string
        pointer, res = 0,0
        dic = {} # key is the char, val is the largest index of the char
        for i, n in enumerate(s):
            if n not in dic:
                dic[n] = i
            else:
                # dabca, when it reach to the second a
                # need to move to the first index of a plus 1
                pointer = max(pointer, dic[n] + 1) 
                # also pwpwkewa when it reach to the last w, the pointer was at second w, but it need to go to the last w, because we want to reset the sub string
                dic[n] = i
            res = max(res, i - pointer + 1)
        return res

# s = Solution()
# print(s.lengthOfLongestSubstring("abcdbac"))
# @lc code=end

