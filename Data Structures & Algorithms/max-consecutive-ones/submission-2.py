class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        ans = c
        for num in nums:
            if num == 1:
                c=c+1
            else:
                c = 0
            ans = max(ans,c)

        return ans