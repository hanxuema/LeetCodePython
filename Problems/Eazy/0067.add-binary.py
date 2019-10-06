#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        carry = 0
        for i in range(max(len(a), len(b))):
            print("i " +str(i))
            val = 0
            if i < len(a):
                val += int(a[- (i + 1)])  # 0 -> 1 -> 0 -> 1
            if i < len(b):
                val += int(b[- (i + 1)])  # 1 -> 1 -> 0 -> 1
        
            val += carry
            if val >= 2 :
                carry = 1
            else:
                carry = 0
            res += str(val % 2)
        if carry == 1:
            res += "1"
        return res[::-1]

# s = Solution()
# print(s.addBinary("11", "1"))
#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result, carry, val = "", 0,0
        for i in  range(max(len(a), len(b))):
            val  = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry, val = val // 2, val % 2
            result += str(val)
        if carry:
            result += str(1)
        return result[::-1]


if __name__ == '__main__':
    print(Solution().addBinary("111", "1"))
