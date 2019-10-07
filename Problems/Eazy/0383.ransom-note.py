#
# @lc app=leetcode id=383 lang=python
#
# [383] Ransom Note
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote is None and magazine is None:
            return False
        lookup = {}
        for n in magazine:
            if n not in lookup:
                lookup[n] = 1
            else:
                lookup[n] += 1
        for n in ransomNote:
            if n not in lookup:
                return False
            elif lookup[n] == 0:
                return False
            else:
                lookup[n] -= 1
        return True
# @lc code=end

