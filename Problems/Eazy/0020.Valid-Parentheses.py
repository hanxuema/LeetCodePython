class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        lookup = {
                    "{":"}",
                    "[":"]",
                    "(":")"
                }

                #[{()}]
        for item in s:
            if item in lookup: # the { [ (
                stack.append(item)
            elif len(stack) == 0 or lookup[stack.pop()] != item:
                return False
        return len(stack) == 0