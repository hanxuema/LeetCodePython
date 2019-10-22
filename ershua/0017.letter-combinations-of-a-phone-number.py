#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        res = []
        if digits is None or len(digits) == 0:
            return res
        keyMap = {
            "0":" ",
            "1":"*",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"            
        }
        sb , index = "", 0
        self.dfs(res, digits, sb, index, keyMap)
        return res
    
    def dfs(self, res, digits, sb, index, keyMap):
        if len(sb) > len(digits):
            return
        if len(sb) == len(digits):
            res.append(sb)
            return
        values = keyMap[digits[index]]
        for i in range(len(values)):
            ss = sb + values[i]
            self.dfs(res,digits,ss,index+1,keyMap)
        
# @lc code=end

s = Solution()
print(s.letterCombinations("23"))