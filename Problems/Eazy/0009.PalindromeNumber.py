class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        # if x is 123
        res = 0
        a = x
        while a != 0:
            temp = a % 10 # 3, 2, 1
            res =  res * 10 + temp # 0 * 10 + 3 = 3, 3 * 10 + 2 = 32, 32 * 10 + 1 = 321
            a = a // 10 # 12, 1, 0
        return res == x

Solution().isPalindrome(121)