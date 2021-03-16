# 题意：最长公共子串问题
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , str1 , str2 ):
        # write code here
        # 最长公共子串，意思要求子串连续
        if not str1 or not str2: return 
        n1,n2 = len(str1), len(str2)
        dp = [[0 for i in range(n2+1)] for i in range(n1+1)]
        max_i,max_len = -1,0
        for i in range(1,n1):
            for j in range(1,n2):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    if dp[i][j]>max_len: 
                        max_i,max_len = i,dp[i][j]
                else:
                    dp[i][j] = 0
        return str1[max_i-max_len+1:max_i+1]