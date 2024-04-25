class Solution(object):
    def maxProfit(self, prices):
        buy_prices = prices[0]
        profit = 0
        n = len(prices)
        for i in range(1,n):
            if prices[i]< buy_prices:
                buy_prices = prices[i]
            elif(prices[i] - buy_prices >profit):
                profit = prices[i] - buy_prices
        return profit    
         
        