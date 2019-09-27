#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # go over whole array, find the min number
        # get the max profile
        max_profile = 0
        min_price = float("inf")

        for price in prices:
            min_price = min(min_price, price)
            max_profile = max(max_profile, price - min_price)
        return max_profile

# if __name__ == '__main__':
#     prices = [7, 1, 5, 3, 6, 4]
#     print(Solution().maxProfit(prices))