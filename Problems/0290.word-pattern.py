#
# @lc app=leetcode id=290 lang=python
#
# [290] Word Pattern
#

# @lc code=start


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # similar to 205 isomorphic strings
        strArray = str.split(' ')
        if len(pattern) != len(strArray):
            return False
        lookup = {}
        lookup2 = {}
        for i in range(len(pattern)):
            if pattern[i] not in lookup:
                lookup[pattern[i]] = strArray[i]
            elif lookup[pattern[i]] != strArray[i]:  # aa, dog,cat
                return False

        for i in range(len(strArray)):
            if strArray[i] not in lookup2:
                lookup2[strArray[i]] = pattern[i]
            elif lookup2[strArray[i]] != pattern[i]:  # aa, dog,cat
                return False
        
        return True


# Solution().wordPattern("abba", "dog dog dog dog")

# @lc code=end
