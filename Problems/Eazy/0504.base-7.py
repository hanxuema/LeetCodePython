#
# @lc app=leetcode id=504 lang=python
#
# [504] Base 7
#
import unittest
# @lc code=start
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        isNagetive =  num < 0
        n = abs(num)
        res = ""
        while n != 0:
            res = str(n % 7) + res
            n = n // 7
        if isNagetive:
            res = "-" + res
        return res
# @lc code=end

class test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.convertToBase7(100),"202")
        self.assertEqual(s.convertToBase7(-7),"-10")

if __name__ == "__main__":
    unittest.main()