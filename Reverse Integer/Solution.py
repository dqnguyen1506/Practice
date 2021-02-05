class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = 0
        if(x < 0): k = -1
        else: k = 1
        while(x != 0):
            x = abs(x)
            pop = x % 10
            x = x//10
            answer = answer * 10 + pop
        return answer * k
sol = Solution()
answer = sol.reverse(-123)
print(answer)
