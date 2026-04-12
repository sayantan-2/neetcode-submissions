class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights)
        areas=[]
        for i in range(l):
            for j in range(i+1,l):
                h = min(heights[i],heights[j])
                b = j-i
                areas.append(h*b)
        return max(areas)