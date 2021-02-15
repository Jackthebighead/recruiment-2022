# 题意：剪绳子问题的大数版，要求最后结果%1000000007
# 由于语言特性，理论上 Python 中的变量取值范围由系统内存大小决定（无限大），因此在 Python 中其实不用考虑大数越界问题
# 但还是写一下大数的解法

class Solution:
    def cuttingRope(self, n):
        # inputs: n: int
        # outputs: int
        import math
        if n <= 3:
            return (n-1)%1000000007
        a = n % 3
        b = n // 3
        if a == 0:
            return 3 ** b % 1000000007
        elif a == 1:
            return 3 ** (b-1) * 4 % 1000000007
        return 3 ** b * 2 % 1000000007


class Solution_2:
    # 快速幂求法
    def remainder_fast(self, x, a, p):
        rem = 1
        while a>0:
            if a%2 == 1:
                rem = (rem * x) % p
            x = x ** 2 % p
            a = a // 2
        return rem

    # 循环求法
    def remainder(self, x, a, p):
        res = 1
        for _ in range(a):
            res = (res * x) % p
        return res

    def cuttingRope(self, n):
        # inputs: n: int
        # outputs: int
        import math
        if n <= 3:
            return (n-1)%1000000007
        a = n % 3
        b = n // 3
        rem = self.remainder(3,b-1,1000000007)
        if a == 0:
            return (rem*3)%1000000007  # 用在这里，或者在之前先把算法后面根据if来调整
        elif a == 1:
            return (rem*4)%1000000007
        return (rem*6)%1000000007