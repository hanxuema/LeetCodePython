#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])):
           for st in strs[1:]:
               if i >= len(st) or strs[0][i] != st[i] :
                   return strs[0][:i]
        
                
s = Solution()
t= ["flower","flow","flight"]
print(s.longestCommonPrefix(t))
