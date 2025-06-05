'''
Approach:

Create a variable maxPro and store 0 initially.
Create a variable minPrice and store some larger value(ex: MAX_VALUE) value initially.
Run a for loop from 0 to n.
Update the minPrice if it is greater than the current element of the array
Take the difference of the minPrice with the current element of the array and compare and maintain it in maxPro.
Return the maxPro.

'''


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float('inf')

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            profit = max(profit, prices[i] - min_price)

        return profit
    

if __name__ == "__main__":
    solution = Solution()
    prices = [7,1,5,3,6,4]
    max_profit = solution.maxProfit(prices)
    print(max_profit)