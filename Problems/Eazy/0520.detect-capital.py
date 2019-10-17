#
# @lc app=leetcode id=520 lang=python
#
# [520] Detect Capital
#

# @lc code=start
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word is None or len(word) == 0 or len(word) == 1:
            return True
        firstCaptial = word[0].isupper()
        
        temp = word[1].isupper()
        for w in word[1:len(word):1]:
            if temp != w.isupper():
                return False
        if firstCaptial == False and temp == True:
            return False
        return True
            
        
# @lc code=end

s = Solution()
print(s.detectCapitalUse("lASDflk"))