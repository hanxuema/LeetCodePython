#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None or len(s) != len(t):
            return False
        lookup = {}
        for i in s:
            if i not in lookup:
                lookup[i] = 1
            else:
                lookup[i] = lookup[i]  + 1

        for i in t:
            if i not in lookup:
                return False
            else:
                lookup[i] =lookup[i] -1
        
        for i in lookup:
            if lookup[i] != 0:
                return False
        
        return True
# @lc code=end

