class Solution(object):
    def getDescentPeriods(self, prices):
        n = len(prices)
        total = 0
        dp = [0] * n
        
        for i in range(n):
            if i > 0 and prices[i] == prices[i-1] - 1:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
            total += dp[i]
        
        return total
