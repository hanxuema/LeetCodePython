#
# @lc app=leetcode id=392 lang=python
#
# [392] Is Subsequence
#

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        pos = 0
        string = list(s)
        for n in t:
            if string[pos] == n:
                pos += 1
            if pos == len(string):
                return True
        return False
    

# Solution().isSubsequence("abc","ahbgdc")

# @lc code=end

