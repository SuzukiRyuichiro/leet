from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      profit = 0
      i, j = 0, 1
      while j < len(prices):
        if prices[i] > prices[j]:
          i += 1
          j += 1
        else:
          while j < len(prices) - 1 and prices[j] < prices[j + 1]:
            j += 1

          profit += prices[j] - prices[i]
          i = j + 1
          j = i + 1

      return profit

sol = Solution()
prices = [1,2,3,4,5,6]
print(sol.maxProfit(prices))
