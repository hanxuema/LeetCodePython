#
# @lc app=leetcode id=551 lang=python
#
# [551] Student Attendance Record I
#
# https://leetcode.com/problems/student-attendance-record-i/description/
#
# algorithms
# Easy (45.93%)
# Likes:    179
# Dislikes: 662
# Total Accepted:    61.5K
# Total Submissions: 133.9K
# Testcase Example:  '"PPALLP"'
#
# You are given a string representing an attendance record for a student. The
# record only contains the following three characters:
#
#
#
# 'A' : Absent.
# 'L' : Late.
# ⁠'P' : Present.
#
#
#
#
# A student could be rewarded if his attendance record doesn't contain more
# than one 'A' (absent) or more than two continuous 'L' (late).
#
# You need to return whether the student could be rewarded according to his
# attendance record.
#
# Example 1:
#
# Input: "PPALLP"
# Output: True
#
#
#
# Example 2:
#
# Input: "PPALLL"
# Output: False
#
#
#
#
#
#

import unittest
# @lc code=start


class Solution(object):
    def checkRecord(self, s):
        if s is None or len(s) <= 1:
            return True
        countA = 0
        for i, n in enumerate(s):
            if n == "A":
                countA += 1
                if countA > 1:
                    return False
            if i <= len(s) - 3 and s[i] == "L" and s[i + 1] == "L" and s[i + 2] == "L":
                return False
        return True

# @lc code=end


class test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual(s.checkRecord("LL"), False)
        self.assertEqual(s.checkRecord("PPALLP"), True)
        self.assertEqual(s.checkRecord("PPALLL"), False)


if __name__ == '__main__':
    # print(8 * 3)
    unittest.main()
