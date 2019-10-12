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
        if ((numerator > 0 and denominator < 0 ) or(numerator < 0 and denominator > 0)):
            res.append("-")
        divisor = abs(numerator)
        dividend = abs(denominator)
        remainder = divisor % dividend

        res.append(str(divisor // dividend)) # 2
        if remainder == 0:
            return "".join(res) # 6/3 = 2

        res.append(".") # else 8/3 =  2.6666666   2.
        lookup = {}
        while remainder != 0:
            if remainder in lookup:  # lookup has {2:0, .:1, 6:1}
                res.insert(lookup[remainder], "(")
                res.append(")")
                break
            else:
                lookup[remainder] = len(res) # 6
                remainder = remainder * 10
                res.append(str(remainder // dividend))  # 2.6
                remainder = remainder % dividend

        return "".join(res)

# s = Solution()
# print(s.fractionToDecimal(2,3))
# @lc code=end

