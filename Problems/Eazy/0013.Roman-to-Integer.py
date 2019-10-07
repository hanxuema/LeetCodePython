class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # create a lookup dic
        lookup = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
        }
        res = 0
        # loop through input s
        for i in range(len(s)):  # convert s from int to string
            if i > 0 and lookup[s[i]] > lookup[s[i - 1]]:
                # if the current value is greater or equal to the previous one, keep adding
                res = res + lookup[s[i]] - 2 * lookup[s[i - 1]]
            else:
                # otherwise, need to minus the previous one 1 time and another time
                res += lookup[s[i]]
        return res


s = Solution()
print(s.romanToInt("MCMXCIV"))
