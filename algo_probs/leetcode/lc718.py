# 题意：最长重复子数组问题
# 题解：这是最长重复子串问题，注意子串是连续的，要与最长公共子序列问题区分开来
# 题解1: 用动态规划转移方程如代码所示
# 题解2: 滑动窗口方法

class Solution:
    def findLength(self, A, B):
        # inputs: A:List[int], B: List[int]
        # outputs: int

        if not A or not B: return 
        n1,n2 = len(A), len(B)
        dp = [[0 for i in range(n2+1)] for i in range(n1+1)]
        max_len = 0
        # 本题从后往前和从前往后是一样的
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    if dp[i][j]>max_len: 
                        max_len = max(max_len,dp[i][j])
                else:
                    dp[i][j] = 0
        return max_len

class Solution_2:
    def findLength(self, A, B):
        # inputs: A:List[int], B: List[int]
        # outputs: int
        # 滑动窗口方法，实际上和dp差不多.O((n1+n2)*min(n1,n2))
        #if not A or not B: return 
        def static_max(start_a,start_b,n):
            res = k = 0
            for i in range(n):
                if A[start_a+i]==B[start_b+i]:
                    k+=1
                    res = max(res,k)
                else: k=0
            return res  # 当前静态串的最长公共子串长度
        
        # 滑动窗口
        # 先让A不动
        res = 0
        n1,n2 = len(A),len(B)
        for i in range(n1):
            temp = min(n1-i,n2)
            res = max(res,static_max(i,0,temp))
        for j in range(n2):
            temp = min(n1,n2-j)
            res = max(res,static_max(0,j,temp))
        return res