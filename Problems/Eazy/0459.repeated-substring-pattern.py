#
# @lc app=leetcode id=459 lang=python
#
# [459] Repeated Substring Pattern
#
import unittest
# @lc code=start
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # return s in (2*s)[1:-1]
        n = len(s)
        a = n // 2
        while a > 0:
            if n % a == 0:
                m = n // a
                if s == s[:a] * m:
                    return True
            a -= 1
        return False

        
# @lc code=end

class TestStringMethods(unittest.TestCase):
       
    def test1and2(self):
        s = Solution()
        self.assertEqual(s.repeatedSubstringPattern("abc"),False)

    def test2(self):
        s = Solution()
        self.assertEqual(s.repeatedSubstringPattern("abab"),True)
    
    def test3(self):
        s = Solution()
        self.assertEqual(s.repeatedSubstringPattern("abcabcabcabc"),True)


if __name__ == '__main__':
    # print(8 * 3)
    unittest.main() 