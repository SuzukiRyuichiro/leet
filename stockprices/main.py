from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        minimumSalesPrice = prices[0]
        maxRevenue = 0

        while j < len(prices):
            revenue = prices[j] - prices[i]
            if revenue > maxRevenue:
                maxRevenue = revenue

            if minimumSalesPrice > prices[j]:
                minimumSalesPrice = prices[j]
                i = j

            j += 1

        return maxRevenue


sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))
