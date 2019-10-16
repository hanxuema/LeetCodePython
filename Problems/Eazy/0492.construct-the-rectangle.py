#
# @lc app=leetcode id=492 lang=python
#
# [492] Construct the Rectangle
#

# @lc code=start
import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # if area == 0:
        #     return [0,0]
        # minVal = area
        # res = []
        # for l in range(1,area+1):
        #     w = area // l
        #     if area % l == 0 and l >= w:
        #         if l-w < minVal:
        #             minVal = l-w
        #             res = [l,w]
        # return res
        mid = int(math.sqrt(area))

        # consider mid to be W here, and until you get to a point where there
        # are exact integers that will equate to a rectangle with area, subtract from mid/W
        # because point 2 states that L >= W
        fuckingShit = area % mid
        while fuckingShit != 0:
            mid -= 1
            fuckingShit = area % mid
    
        # compute L from W (mid), and W (mid)
        return [int(area/mid),mid]

# @lc code=end
s = Solution()
print(s.constructRectangle(5))

