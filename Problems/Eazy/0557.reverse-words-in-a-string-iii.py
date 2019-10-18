#
# @lc app=leetcode id=557 lang=python
#
# [557] Reverse Words in a String III
#
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (65.76%)
# Likes:    720
# Dislikes: 72
# Total Accepted:    151.7K
# Total Submissions: 230.8K
# Testcase Example:  '"Let\'s take LeetCode contest"'
#
# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.
# 
# Example 1:
# 
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# 
# 
# 
# Note:
# In the string, each word is separated by single space and there will not be
# any extra space in the string.
# 
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        if s is None or len(s) <= 1:
            return s
        words = s.split(" ")
        for i, w in enumerate(words):
            words[i] = self.reverseWord(w)
        return " ".join(words)
    
    def reverseWord(self, word):
        if len(word) == 1:
            return word
        return word[::-1]

# @lc code=end

