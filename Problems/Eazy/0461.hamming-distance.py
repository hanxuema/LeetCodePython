#
# @lc app=leetcode id=461 lang=python
#
# [461] Hamming Distance
#
import unittest
# @lc code=start
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        print("{0:b} x".format(x))
        print("{0:b} y".format(y))
        t = x ^ y
        print("{0:b} t".format(t))
        res = 0
        while t > 0:
            res += t % 2
            print("{0:b} res".format(res))
            t = t // 2
            print("{0:b} t".format(t))
        return res
# @lc code=end

class testclass(unittest.TestCase):
    def test1(self):
        s = Solution()
        s.hammingDistance(1,4)

if __name__ == "__main__":
    unittest.main()

