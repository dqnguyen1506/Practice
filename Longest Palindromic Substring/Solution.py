class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(len(s) == 1 or len(s) == 2):
            return s[0]
        mp = {}
        ret_mp = {}
        i = 0
        for j in range (len(s)):
            mp[s[j]] = j
            if(s[i] in mp and s[i] == s[j]):
                ret_mp[j + 1 -i] = s[i:j + 1]
                print("s[i] ", s[i])
                i += 1
        print(ret_mp)
                
             
        
        

sol = Solution()
sol.longestPalindrome("babad")
