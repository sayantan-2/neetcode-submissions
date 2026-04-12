class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
            
        seq=[]
        for i in nums:
            count = 0
            while i+1 in nums:
                count+=1
                i+=1
            seq.append(count+1)
        return (max(seq))

