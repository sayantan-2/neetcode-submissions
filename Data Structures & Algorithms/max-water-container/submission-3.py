class Solution:
    def maxArea(self, heights: List[int]) -> int:
            l=len(heights)
            left=0
            right=l-1
            area=0
            while left<right:
                area=max(area,(right-left)*min(heights[left],heights[right]))

                if heights[left]<heights[right]:
                    left+=1
                else:
                    right-=1

            return area