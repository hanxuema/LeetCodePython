#
# @lc app=leetcode id=455 lang=python
#
# [455] Assign Cookies
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        pointer1, pointer2 = 0,0
        while (pointer1 < len(g) and pointer2 < len(s)):
            if g[pointer1]<= s[pointer2]:
                pointer1 += 1
                pointer2 += 1
            else:
                pointer2+= 1
        return pointer1
# @lc code=end

