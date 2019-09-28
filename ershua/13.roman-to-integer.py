#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        lookup = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        res = lookup[s[0]]
        for i in range(1, len(s)):
            if lookup[s[i]] <= lookup[s[i-1]]:
                res += lookup[s[i]]
            else:
                res += lookup[s[i]] - lookup[s[i-1]] - lookup[s[i-1]]
        return res
