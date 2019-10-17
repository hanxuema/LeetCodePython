#
# @lc app=leetcode id=521 lang=python
#
# [521] Longest Uncommon Subsequence I 
#

# @lc code=start
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a),len(b))
# @lc code=end

