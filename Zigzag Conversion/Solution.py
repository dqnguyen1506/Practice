import math

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        list1 = []
        num = -1
        index = 0
        mp = {}
        for i in range(numRows):
            mp[i] = []
        while (index < len(s)):
            for y in range(numRows):
                num += 1
                if (num == numRows):
                    num = (numRows - 2) * - 1
                    
                    print("num: ", num)

                
                list1 = mp[abs(num)]
                list1.append(index)
                mp[abs(num)] = list1
                index += 1
                if(index == len(s)):
                    break
                if(numRows == 1):
                    return s
        answer = ''
        for x,y in mp.items():
            print(x,y)
            for i in y:
                answer += s[i]
        print(answer)
        return answer
                
        
            

                    
              
                    
                    
sol = Solution()
sol.convert("AB", 1)