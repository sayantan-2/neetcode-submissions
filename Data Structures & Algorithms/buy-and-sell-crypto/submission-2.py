class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0

        for i in range(1,len(prices)):
            curr=prices[i]
            if curr<buy:
                buy=curr
            elif curr-buy>profit:
                profit=curr-buy
            
        return profit