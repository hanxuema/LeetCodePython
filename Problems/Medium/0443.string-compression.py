#
# @lc app=leetcode id=443 lang=python
#
# [443] String Compression
#

# @lc code=start
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i, count = 0,1
        for j in range(1, len(chars)+1):
            if j < len(chars) and chars[j] == chars[j-1]:
                count+=1
            else:
                chars[i] = chars[j-1]
                i+=1
                if count > 1:
                    for m in str(count):
                        chars[i] = m
                        i+=1
                count = 1
        return i
# s = Solution()
# print(s.compress(["a","a","a","b","b","a","a"]))
# @lc code=end

