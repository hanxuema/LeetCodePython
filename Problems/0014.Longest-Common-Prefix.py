class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or len(strs) == 0:
            return ""
       
        for i in range(len(strs[0])):
            for str in strs:
                if len(str) <= i or strs[0][i] != str[i]:
                    return str[0][:i]
        return strs[0]

s = Solution()
t= ["flower","flow","flight"]
print(s.longestCommonPrefix(t))