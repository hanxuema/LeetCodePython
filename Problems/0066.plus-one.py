#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        digits[0] = 11
        digits.append(0)
        return digits
