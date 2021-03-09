# 题意：股票的最大利润
# 题解：动态规划

class Solution:
    def maxProfit(self, prices):
        # inputs: prices: List[int]
        # outputs: int
        # dp
        if not prices: return 0
        h_min = prices[0]
        dp = [0 for _ in range(len(prices))]
        for i in range(1,len(prices)):
            if h_min>prices[i]: h_min=prices[i]
            dp[i] = max(dp[i-1],prices[i]-h_min)
        return dp[len(prices)-1]
            


