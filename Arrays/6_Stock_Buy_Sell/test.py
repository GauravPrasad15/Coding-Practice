from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float('inf')

        for i in range(len(prices)):
            if prices[i] <= min_price:
                min_price = prices[i]
            elif prices[i] - min_price > profit:
                profit = prices[i] - min_price

        return profit
    

if __name__ == "__main__":
    solution = Solution()
    prices = [7,1,5,3,6,4]
    max_profit = solution.maxProfit(prices)
    print(max_profit)