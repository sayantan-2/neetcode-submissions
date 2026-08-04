class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l=len(nums)
        result=[]
        for i in range(l):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
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
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
        return result
