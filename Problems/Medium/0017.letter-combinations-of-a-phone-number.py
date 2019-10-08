#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
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
        res = []
        for d in digits:
            if len(res) == 0:
                for c in keyMap[d]:
                    res.append(c)
            else:
                temp = []
                for r in res:
                    for c in keyMap[d]:
                        temp.append(r+c)
                res = temp
        return res
        
# @lc code=end

