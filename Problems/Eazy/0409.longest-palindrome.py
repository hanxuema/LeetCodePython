#
# @lc app=leetcode id=409 lang=python
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup  = {}
        for n in s:
            if n in lookup:
                lookup[n] += 1
            else:
                lookup[n] = 1
        res = 0
        hasOdd = False
        for l in lookup.keys():
            if lookup[l] % 2 == 1:
                hasOdd = True
            res += lookup[l] // 2 * 2
        return res + 1 if hasOdd else res

# @lc code=end
