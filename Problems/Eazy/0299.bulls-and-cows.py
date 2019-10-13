#
# @lc app=leetcode id=299 lang=python
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        cows, bulls = 0,0
        cowDic, bullDic = {} , {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] in bullDic:
                    bullDic[secret[i]] += 1
                else:
                    bullDic[secret[i]] = 1
                if guess[i] in cowDic:
                    cowDic[guess[i]] += 1
                else:
                    cowDic[guess[i]] = 1
        
        for k in bullDic:
            if k in cowDic:
                cows += min(bullDic[k], cowDic[k])

        return "{}A{}B".format(str(bulls),str(cows))
        
# @lc code=end

