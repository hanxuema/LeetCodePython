#
# @lc app=leetcode id=345 lang=python
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        lookup = {'a','e','i','o','u','A','E','I','O','U'}
        string = list(s)
        left, right  = 0, len(s) -1 
        while left < right:
            if string[left] not in lookup:
                left += 1
            if string[right] not in lookup:
                right -= 1
            if string[left] in lookup and string[right] in lookup:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1
        return "".join(string)
# @lc code=end

