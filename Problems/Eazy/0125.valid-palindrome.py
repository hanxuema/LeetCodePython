#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#
class Solution(object):
    def isPalindrome(self, s):
        if s is None:
            return True
        left, right = 0, len(s) -1
        while left <= right:
            # filter all the prefix none number none alpha char
            while left <= right and not s[left].isalnum():
                left += 1
            # filter all the sufix none number none alpha char
            while left <= right and not s[right].isalnum():
                right -= 1
            # compare
            if left <= right and s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True

