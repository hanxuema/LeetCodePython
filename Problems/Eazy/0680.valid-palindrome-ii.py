#
# @lc app=leetcode id=680 lang=python
#
# [680] Valid Palindrome II
#

# @lc code=start
import unittest
class Solution(object):
    def validPalindrome(self, s):
        left, right = 0, len(s) -1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.helper(self, s, left +1 ,right) or self.helper(self, s, left, right-1)
        return True

    def helper(self, s, left, right):
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        
# @lc code=end

class testClass(unittest.TestCase):
    def test1and2(self):
        s = Solution()
        self.assertEqual(s.validPalindrome("aba"), True)


if __name__ == "__main__":
    unittest.main()