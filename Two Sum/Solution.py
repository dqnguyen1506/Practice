class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos = 0
        mp = {}
        total = 0
        while(pos < len(nums)):
            if (target - nums[pos]) not in mp:
                mp[nums[pos]] = pos
            mp[nums[pos]] = pos
            pos += 1
        for x,y in mp.items():
            print(x,y)

sol = Solution()
sol.twoSum([2,7,11,15], 9)       