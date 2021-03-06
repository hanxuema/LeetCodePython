#
# @lc app=leetcode id=434 lang=python
#
# [434] Number of Segments in a String
#

# @lc code=start
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            if (i == 0 or s[i-1] == " ") and s[i] != " ":
                count += 1
        return count
        
# @lc code=end

