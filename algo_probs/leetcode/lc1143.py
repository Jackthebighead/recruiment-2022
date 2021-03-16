# 题意：最长公共自序列问题
# 题解1: 动态规划

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        n1,n2 = len(text1),len(text2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        max_len = 0
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    max_len = max(max_len,dp[i][j])
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                #max_len = max(max_len,dp[i][j])
        return max_len