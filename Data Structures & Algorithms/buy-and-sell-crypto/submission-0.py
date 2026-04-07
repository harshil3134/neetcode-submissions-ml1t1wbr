class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=10000
        currentProfit=0

        for i in range(0,len(prices)):

            minPrice=min(minPrice,prices[i])

            currentProfit=max(currentProfit,prices[i]-minPrice)

        return currentProfit;