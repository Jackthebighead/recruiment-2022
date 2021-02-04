# 题意：斐波那契数列，青蛙跳台阶问题。
# 解法：递归

class Solution:
    def fib(self, n):
        # input: n: int
        # output: int
        res = [0,1]
        for i in range(2,n+1):
            res.append(res[i-1] + res[i-2])
        return res[n]%1000000007