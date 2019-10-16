#
# @lc app=leetcode id=482 lang=python
#
# [482] License Key Formatting
#

# @lc code=start
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.replace("-","").upper()[::-1]
        res = ""
        for i in range(len(s)):
            res = s[i]+res
            if (i + 1) % K == 0 and i != len(s) -1:
                res= "-" + res
            print("{} {} i res".format(i, res))
        return res
            
# @lc code=end

s = Solution()
print(s.licenseKeyFormatting("5F3Z-2e-9-w",4))