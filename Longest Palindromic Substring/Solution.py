class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(len(s) < 1):
            return ""
        start = 0 
        end = 0
        for i in range (len(s)):
            len1 = self.expandFromMiddle(s, i, i)
            len2 = self.expandFromMiddle(s, i, i + 1)
            length = max(len1, len2)
            print("len1: ", len1)
            print("len2: ", len2)
            if (length > (end - start)):        #racecar #abaaba
                start = i - ((length - 1)//2)
                end = i + (length //2)
        print(start, end)
        return s[start:end + 1]
    def expandFromMiddle(self, s, left, right):
        if(len(s) == 0 or left > right):
            return 0
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
            #print(left)
            #print(right)
        return right - left - 1
sol = Solution()
answer = sol.longestPalindrome("racecar")
print(answer)


