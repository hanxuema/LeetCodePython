#
# @lc app=leetcode id=389 lang=python
#
# [389] Find the Difference
#

# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == len(t):
            return ""
        lookup = {}
        for n in s:
            if n in lookup:
                lookup[n] += 1
            else:
                lookup[n] = 1
        for n in t:
            if n not in lookup:
                return n
            elif lookup[n] == 0:
                return n
            else:
                lookup[n] -= 1
        return ""

# @lc code=end

