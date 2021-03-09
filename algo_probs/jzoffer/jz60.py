# 题意：n个骰子的点数概率。把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
# 题解：动态规划。注意到扔第x个骰子时，点数为[x:6*x+1]，而每一点的概率是上一状态(扔x-1个骰子)的状态加上当前的概率(1/6，1/6)。所以状态转移方程为dp[i][j] = df[i-1][j-1~6]，其中i代表投置第i个骰子，j代表和。
# 状态转移方程

class Solution:
    def dicesProbability(self, n):
        # inputs: n: int
        # outputs: List[float]
        dp = [[0 for _ in range(6*n+1)] for _ in range(n+1)]
        for i in range(1,7): dp[1][i] = 1
        for i in range(2,n+1):
            for j in range(i,6*i+1):
                for k in range(1,7):
                    dp[i][j] += dp[i-1][j-k]
        res = []
        for i in range(n,6*n+1): res.append(dp[n][i]*1.0/(6)**n)
        return res