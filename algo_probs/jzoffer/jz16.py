# 题意：实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。
# 题解1：快速幂方法（同jz12），即用二分法的思想求幂运算，时间复杂度为logn
# 题解1另一种理解：按二进制理解，将输入的n看作：n = 1b_1 + 2b_2 + 4b_3 + ... + 2^{m-1}b_m，我们求x^n。
# 那么每个b_1不是0就是1，我们每次做n&1或者用n%2看每一位是否为1，若为1则存x，不为1则x=x*x，然后再舍弃最低位，即 n>>1，或写成n//2。

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # inputs: x: float, n: int
        # outputs: float
        res = 1
        flag = True
        if n<0:
            n = -n
            flag = False
        while n!=0:
            if n%2:
                res *= x
            x *= x  # 不能用**2，会报错溢出
            n //= 2  # 若用二进制来理解，这里也可以写为：n = n>>1
        return res if flag else 1/res