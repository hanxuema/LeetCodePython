#
# @lc app=leetcode id=93 lang=python
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution(object):
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 0, "", res)
        return res
    
    def dfs(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return # backtracking
        for i in range(1, 4):
            # the digits we choose should no more than the length of s
            if i <= len(s):
                #choose one digit
                ss = s[i:]
                pp = path+s[:i]+"."
                if i == 1: 
                    self.dfs(ss, index+1, pp, res)
                #choose two digits, the first one should not be "0"
                elif i == 2 and s[0] != "0": 
                    self.dfs(ss, index+1, pp, res)
                #choose three digits, the first one should not be "0", and should less than 256
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(ss, index+1, pp, res)

        
# @lc code=end
s = Solution()
print(s.restoreIpAddresses("25525511135"))
