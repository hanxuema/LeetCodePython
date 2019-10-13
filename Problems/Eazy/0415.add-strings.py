#
# @lc app=leetcode id=415 lang=python
#
# [415] Add Strings
#

# @lc code=start
class Solution(object):
    def addStrings(self, num1, num2):
        res=""
        i,j,carry = len(num1)-1, len(num2)-1, 0
        while i >=0 or j>=0:
            n1 = num1[i] if i>=0 else "0"
            n2 = num2[j] if j>=0 else "0"
            sums = int(n1) + int(n2) + carry
            res = str(sums % 10) + res
            carry = sums // 10
            i-=1
            j-=1
        if carry == 1:
            res = "1"+res
        return res 

       

# s = Solution()
# print(s.addStrings("98","9"))
# @lc code=end

