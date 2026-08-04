class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        p=0
        for i in range(l-1):
            price = prices[i]
            m=max(prices[i+1:])
            p=max(p,(m-price))
        return p