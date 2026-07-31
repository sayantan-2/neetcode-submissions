class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        left=[1]
        right=[0]*l
        right[l-1]=1
        for i in range(1,l):
            left.append(left[i-1] * nums[i-1])
            j=-(i+1)
            right[j]=right[-i]*nums[-i]

        answer=[]
        for i in range(l):
            answer.append(left[i]*right[i])
        # print(left)
        # print(right)
        return answer