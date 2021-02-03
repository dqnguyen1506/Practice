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
        res = [[] for i in range(numRows)]              #initilize the list of lists *
        for char in s:
            print(currRow)
            res[currRow].append(char)
            if(currRow == 0 or currRow == numRows - 1): #if current row hits the beginning or the end
                delta *= -1                             #change direction
            currRow += delta                                
        answer = ''
        for i in res:                                   #join the lists
            answer += ''.join(i)
        print (answer)
        return answer

        
sol = Solution()
sol.convert("PAYPALISHIRING", 4)