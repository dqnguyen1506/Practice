import array as arr
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        mp = {}
        i = 0
        for j in range (len(s)):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            answer = max(answer, j - i + 1)
            mp[s[j]] = j + 1
        print(answer)
        for x,y in mp.items():
            print(x,y)
        


        
                

        
def main():
    sol = Solution()
    sol.lengthOfLongestSubstring('pwwkew')
   

main()