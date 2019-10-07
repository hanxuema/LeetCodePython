#
# @lc app=leetcode id=168 lang=python
#
# [168] Excel Sheet Column Title
#

# @lc code=start


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        base = 26
        res = ""
        while n:
            res =  chr(ord('A') + ((n - 1) % base)) + res
            n = (n-1) // base
        return res


# if __name__ == "__main__":
#     # for i in range(1, 2999):
#     print(str(79) + " " + Solution().convertToTitle(26))
# # @lc code=end
