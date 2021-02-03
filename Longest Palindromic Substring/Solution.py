class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        list1 = []
        length = 0
        answer = ''
        for x in range (len(s)):
            list1.append(s[x])
            for y in range(x+1,len(s)):
                list1.append(s[y])
                list2 = list1[::-1]
                if(list1 == list2 and len(list1) > length):
                    length = len(list1)
                    answer = ''.join(list1)
                if(y == len(s) - 1):
                    list1 = []
        if(len(s) == 1 or length == 1):
            return s[0]
        print(answer)
        return answer                       
sol = Solution()
print(sol.longestPalindrome("ac"))

