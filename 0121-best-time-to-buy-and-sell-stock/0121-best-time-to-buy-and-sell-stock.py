class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        max_price = float('-inf')

        i = 1

        if (len(prices)==1):
            return 0

        while (i<len(prices)):

            if (prices[i] < min_price):
                min_price = prices[i]

            profit = prices[i] - min_price
            if profit >= max_price and profit >=0:
                max_price = profit
            
            i+=1

        return max_price