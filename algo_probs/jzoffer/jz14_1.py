# 题意：剪绳子，给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
# 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
# 题解1: 动态规划。注意到我们所求的乘积可以当作动态规划中的状态。设置1-n的状态数组dp[n]在存，动态归化的状态方程是：dp[i] = max(dp[i-j]*j, (i-j)*j)即对于一段长度i的绳子，其最大乘积dp[i]
#       可以分为对这一段进行裁剪和不裁剪两种情形，对于裁剪情形，我们可以设置另一个指针去循环，得到的中间结果存入dp对以后的判别都有用。dp实际上也是一个查表算数的过程。
# 题解2: 数学方法，通过不等式原理可以知道一段绳子分成尽可能等长时乘积最大，通过求导证明得当这个等长为3的时候最优。所以接下来需要考虑的就是若不能整除3余数分别为12时候的情形。

class Solution:
    def cuttingRope(self, n):
        # inputs: n: int
        # outputs: int
        import math
        if n <= 3:
            return n-1
        a = n % 3
        b = n // 3
        if a == 0:
            return int(math.pow(3,b)) # math.pow()算的更快
        elif a == 1:
            return int(math.pow(3,b-1)*4)
        return int(math.pow(3,b)*2)


class Solution_2:
    def cuttingRope(self, n):
        # inputs: n: int
        # outputs: int
        dp = [0 for _ in range(n+1)]  # n+1为界限不是n
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(i):
                dp[i] = max(dp[i],max(j*dp[i-j],j*(i-j)))
        return dp[n]
