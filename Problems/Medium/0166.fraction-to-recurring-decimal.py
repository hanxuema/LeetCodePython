#
# @lc app=leetcode id=166 lang=python
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0 or denominator == 0:
            return "0"
        res = []
        if ((numerator > 0 and denominator < 0) or (numerator<0 and denominator >0) ):
            res.append("-")
        divisor = abs(numerator) #2
        dividend = abs(denominator) #3
        res.append(str(divisor // dividend)) #0
        remainder = divisor % dividend # 2
        if remainder == 0:
            return "".join(res)
        res.append(".")
        lookup = {}
        while remainder != 0: 
            if remainder in lookup:
                res.insert(lookup[remainder],"(")
                res.append(")")
                break
            lookup[remainder] = len(res) #res = [0, . , ] {2:2}
            remainder *= 10  # 2 * 10 = 30
            res.append(str(remainder // dividend))  # [0.6]
            remainder %= dividend
        
        return "".join(res)

s = Solution()
print(s.fractionToDecimal(2,3))
# @lc code=end

