import math
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        print(len(s))
        list1 = []
        inc = ((numRows - 1) + (numRows - 2))
        i = 0
        while (i < (len(s) - inc)):
            print(i)
            print(inc + i)
            list1.append(s[i])
            list1.append(s[inc + i])
            i+=1
        print(list1)

sol = Solution()
sol.convert("PAHNAPLSIIGYIR", 4)