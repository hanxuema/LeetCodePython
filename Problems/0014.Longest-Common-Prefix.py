class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or len(strs) == 0:
            return ""
        
        for idx in range(len(strs[0])):
            for str in strs:
                if len(str) <= idx or strs[0][idx] != str[idx]:
                    return strs[0][:idx]
        return strs[0]

s = Solution()
t= ["aa","a"]
print(s.longestCommonPrefix(t))