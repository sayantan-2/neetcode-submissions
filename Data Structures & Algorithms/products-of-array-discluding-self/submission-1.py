class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)

        output=[]
        for i in range(l):
            prd=1
            for j in range(l):
                if i!=j:
                    prd=prd*nums[j]
            output.append(prd)

        return output
        