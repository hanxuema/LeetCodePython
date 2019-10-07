#
# @lc app=leetcode id=171 lang=python
#
# [171] Excel Sheet Column Number
#

# @lc code=start


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)):
            result = result * 26
            result = result + ord(s[i]) - ord("A") +1
        return result


# if __name__ == "__main__":
#     print(Solution().titleToNumber("AB"))
# @lc code=end
