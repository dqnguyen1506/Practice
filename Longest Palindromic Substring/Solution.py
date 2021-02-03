class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(len(s) == 1):
            return s[0]
        list1 = []
        mp = {}
        i = 0
        length = 0
        answer = ''
        for x in range (len(s)):
            list1.clear()
            for y in range(len(s)):
                if(y >= x):
                    list1.append(s[y])
                    list2 = list1[::-1]
                    if(list1 == list2 and len(list1) > length):
                        length = len(list1)
                        answer = ''.join(list1)
        print(answer)
        return answer                       
sol = Solution()
sol.longestPalindrome("bb")
