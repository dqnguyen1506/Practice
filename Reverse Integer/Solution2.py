class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x < 0): k = -1
        else: k = 1
        x = int(str(abs(x))[::-1])
        if(x <= -2**31 or x >= 2**31 - 1):
            return 0
        return x * 