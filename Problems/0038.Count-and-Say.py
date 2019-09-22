class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 1.     1
        # 2.     11
        # 3.     21
        # 4.     1211
        # 5.     111221
        # 6.     312211
        res = "1"
        for i in range(n - 1): #if n is 4,  (0,4)
            res = self.convert(res)
            print(str.format("i {0}, res {1}", str(i), res))
        return res

    def convert(self, res):
        i, next = 0, ""
        while i < len(res): # same as for each
            # prevent out of range
            count = 1
            while i < len(res) - 1 and res[i] == res[i + 1]:
                # sub loop for the same continues int
                count += 1
                i += 1
            next = next + str(count) + res[i] # how many 1 + last index of current number
            i += 1
        return next
            
        


s = Solution()
print(s.countAndSay(5))
