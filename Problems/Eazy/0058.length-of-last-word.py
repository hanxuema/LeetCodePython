#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# this is slow from Michelle 
# class Solution(object):
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) == 0:
#             return 0
#         count = 0
#         localCount = 0
#         for i in range(len(s)):
#             if s[i] == " ":
#                 localCount = 0
#             else:
#                 localCount += 1
#                 count = localCount
#         return count



class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        countOfLeadingEmpty = 0
        firstNonEmpty = False
        i = 0
        for c in reversed(s):
            if c != " " and firstNonEmpty == False:
                 firstNonEmpty= True
            if c == " " and firstNonEmpty == False:
                countOfLeadingEmpty  += 1
            elif c == " ":
                    return i - countOfLeadingEmpty
            i += 1
        return i - countOfLeadingEmpty
# s = Solution()
# print(s.lengthOfLastWord(" "))
