class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(0,l):
            new = target-nums[i]

            for j in range(i+1,l):
                if nums[j]==new:
                    return [i,j]
            

        