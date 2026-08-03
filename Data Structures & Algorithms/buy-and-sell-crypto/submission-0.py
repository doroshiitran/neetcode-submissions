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
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] > prices[i]:
                    max_profit= max(prices[j]-prices[i], max_profit)
        return max_profit