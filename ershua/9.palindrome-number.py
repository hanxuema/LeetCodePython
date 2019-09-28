#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        newNumber =  0
        a = x
        while a != 0:
            lastDigit = a  % 10
            newNumber = newNumber * 10 + lastDigit
            a = a // 10
        return x == newNumber
        

