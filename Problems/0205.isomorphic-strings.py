#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#

# @lc code=start


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
            return False
        if len(s) != len(t):
            return False
        return self.checkIsomorphic(s, t) and self.checkIsomorphic(t, s)

    def checkIsomorphic(self, left, right):
        lookup = {}
        print(left)
        for i in range(len(left)):
            if left[i] not in lookup:
                lookup[left[i]] = right[i]
            elif lookup[left[i]] != right[i]:
                return False
        return True


# Solution().isIsomorphic("abc", "dfg")
# @lc code=end
