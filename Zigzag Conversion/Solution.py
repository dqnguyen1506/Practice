class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if (numRows == 1):
            return s
        currRow = 0
        delta = -1
        res = [[] for i in range(numRows)]
        for char in s:
            print(currRow)
            res[currRow].append(char)
            if(currRow == 0 or currRow == numRows - 1):
                delta *= -1
            currRow += delta
        answer = ''
        for i in res:
            answer += ''.join(i)
        print (answer)
        return answer

        
sol = Solution()
sol.convert("PAYPALISHIRING", 4)