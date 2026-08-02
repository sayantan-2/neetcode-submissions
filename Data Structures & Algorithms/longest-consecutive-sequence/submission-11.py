class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique=set(nums)
        longest = 0
        count = 0
        for num in nums:
            if num-1 not in unique:
                count=1
                while num+count in unique:
                    count+=1
            if count > longest:
                longest=count
        return longest