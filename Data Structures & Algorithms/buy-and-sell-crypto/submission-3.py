class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0

        for i in range(1,len(prices)):
            curr=prices[i]
            profit=max(profit,curr-buy)
            buy=min(buy,curr)
            
        return profit