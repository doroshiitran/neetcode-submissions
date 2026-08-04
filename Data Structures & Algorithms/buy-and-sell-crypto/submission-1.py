class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        brute force - O(n^2)
        1 pointer i as 0, 1 pointer j=i+1
        while i and j <= range(len(prices)) =>
        max_profit=0
        if prices[j]>prices[i]: max(prices[j]-prices[i], max_profit)
        else j++
        """
        max_profit=0
        l, r =0,1
        while r < len(prices):
            if prices[r]> prices[l]:
                max_profit= max(prices[r]-prices[l], max_profit)
            else:
                l = r
            r+=1
        return max_profit