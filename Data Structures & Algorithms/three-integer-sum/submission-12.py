class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l=len(nums)
        result=[]
        for i in range(l):
            target = -nums[i]
            j=i+1
            k=l-1
            while j<k:
                total = nums[j]+nums[k]
                if total>target:
                    k-=1
                elif total<target:
                    j+=1
                else:
                    if [nums[i],nums[j],nums[k]] not in result:
                        result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
        return result