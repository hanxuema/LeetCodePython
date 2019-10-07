#
# @lc app=leetcode id=412 lang=python
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        three, five, threeFive = "Fizz","Buzz","FizzBuzz"
        res = []
        for i in range(1, n + 1):
            temp = str(i)
            if i % 15 == 0:
                temp = threeFive
            elif i % 3 == 0:
                temp = three
            elif i % 5 == 0:
                temp = five
            res.append(temp)
        return res
# @lc code=end

