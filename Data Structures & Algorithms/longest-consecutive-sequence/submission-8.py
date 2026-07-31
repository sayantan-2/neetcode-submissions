class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        uniques = set(nums)
        s = sorted(uniques)
        l = len(s)
        count = 0
        seq=[]
        for i in range(l-1):
            if s[i]+1 == s[i+1]:
                count+=1

            else:
                seq.append(count+1)
                count=0
        seq.append(count + 1)
        return max(seq)