class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1] *(n+1)

        return self.func(n,dp)

    def func(self , n , dp):

        if n==0 or n==1:

            return 1
        
        if dp[n]!= -1:
            return dp[n]
        
        dp[n] = self.func(n-1,dp) + self.func(n-2,dp)
        return dp[n]