#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ""
        if len(s) == 1:
            return s[0]
        
        res = ""
        for i, n in enumerate(s):
            #1 aba
            temp1 = self.checkPalindrome(s, i, i)
            #2 abba
            temp2 = self.checkPalindrome(s, i, i + 1)
            if len(temp1) > len(temp2):
                temp2 = temp1
            if len(temp2) > len(res):
                res = temp2
        return res

    def checkPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]
        

# s = Solution()
# s.longestPalindrome("ccc")
# @lc code=end

