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
                i = max(i, mp[s[j]])
            mp[s[j]] = j + 1
            answer = max(answer, j - i + 1)
        print(answer)
        


        
                

        
def main():
    sol = Solution()
    sol.lengthOfLongestSubstring('pwwkew')
   

main()