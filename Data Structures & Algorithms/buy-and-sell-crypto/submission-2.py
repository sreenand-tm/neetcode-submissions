class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        mp=0
        s=1
        while(s<len(prices)):
            if(prices[s]<prices[b]):
             b=s
            if(prices[s]>prices[b] and (prices[s]-prices[b])>mp):
             mp=prices[s]-prices[b]
            s=s+1
        return mp
