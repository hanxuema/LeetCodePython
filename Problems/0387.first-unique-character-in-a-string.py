#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {}
        for n in s:
            if n in lookup:
                lookup[n] += 1
            else:
                lookup[n] = 1
        
        for i, n in enumerate(s):
            if lookup[n] == 1:
                return i
        return -1
# @lc code=end

