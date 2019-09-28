#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """ 
        if len(s) % 2 == 1:
            return False
        lookup = {
            '{' : '}',
            '[' : ']',
            '(' : ')'
        }
        stack = []
        for p in s:
            if p in lookup: # can be found in lookup, means { ( [ 
                stack.append(p)
            elif len(stack) == 0 or lookup[stack.pop()] != p:
                return False
        return len(stack) == 0


Solution().isValid("()")