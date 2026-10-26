class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, current_profit, min_price, max_profit = 0, 0, float('inf'), 0
        for price in prices:
            min_price = min(min_price, price)
            current_profit = price - min_price
            
            max_profit = max(max_profit, current_profit)
            
        

        return max_profit