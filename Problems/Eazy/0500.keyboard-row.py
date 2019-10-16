#
# @lc app=leetcode id=500 lang=python
#
# [500] Keyboard Row
#
# https://leetcode.com/problems/keyboard-row/description/
#
# algorithms
# Easy (62.98%)
# Likes:    435
# Dislikes: 548
# Total Accepted:    96.5K
# Total Submissions: 153.2K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# Given a List of words, return the words that can be typed using letters of
# alphabet on only one row's of American keyboard like the image below.
# 
# 
# 
# 
# 
# 
# Example:
# 
# 
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# 
# 
# 
# 
# Note:
# 
# 
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
# 
# 
#
import unittest
# @lc code=start
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) == 0:
            return []
        res = []

        for w in words:
            if self.isWordInOneRow(w):
                res.append(w)
        return res
    
    def isWordInOneRow(self, word):
        if word is None or len(word) == 0:
            return True
        lookup = {
            'Q':1,'W':1,'E':1,'R':1,'T':1,'Y':1,'U':1,'I':1,'O':1,'P':1,
            "A":2,"S":2,"D":2,"F":2,"G":2,"H":2,"J":2,"K":2,"L":2,
            "Z":3,"X":3,"C":3,"V":3,"B":3,"N":3,"M":3,
        }
        pre = lookup[word[0].upper()]
        for w in word.upper():
            row = lookup[w]
            if row != pre:
                return False
        return True

# @lc code=end

class testclass(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertFalse(s.isWordInOneRow("Hello"))
        self.assertFalse(s.isWordInOneRow("Peace"))
        self.assertTrue(s.isWordInOneRow("Alaska"))
        self.assertTrue(s.isWordInOneRow("Dad"))
        self.assertEqual(s.findWords(["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"])

if __name__ == "__main__":
    unittest.main()