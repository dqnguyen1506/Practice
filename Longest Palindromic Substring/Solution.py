class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(len(s) <  1):
            return ''
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandFromMiddle(s,i,i) #racecar
            len2 = self.expandFromMiddle(s,i,i+1) #abaaba
            length = max(len1, len2)
            if(length > end - start):
                start = i - ((len(s) - 1)//2)
                end = i + len(s)//2
                print(start)
                print(end)
        return s[start:end + 1]
    def expandFromMiddle(self, s, left, right):
        if(left > right or len(s) == 0 ):
            return 0
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1
sol = Solution()
answer = sol.longestPalindrome("racecar")

print(answer)


