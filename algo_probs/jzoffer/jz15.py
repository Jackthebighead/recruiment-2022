# 题意：请实现一个函数，输入一个整数（以二进制串形式），输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。
# 题解1: 注意输入的是int的10进制整数，所以用python的话要转换成2进制，可以用bin()函数转换为二进制的字符串，然后在用字符串的count()函数统计1的个数返回即可
# 题解2: 还可以用python的位运算符，按位运算符是把数字看作二进制来进行计算的。& | ^ ~ << >>分别表示按位与，或，异或，取反，向左移动，高位丢低位补
# 题解3: 用n&n-1操作。因为二进制条件下，n和n-1字符相与可以让n的最后一个1为0，其他不变，while循环至n为0即可

class Solution:
    def hammingWeight(self, n):
        # inputs: n: int
        # outputs: int
        return bin(n).count('1')

class Solution_2:
    def hammingWeight(self, n):
        # inputs: n: int
        # outputs: int
        res = 0
        while n:
            res += n & 1
            n = n >> 1
        return res

class Solution_3:
    def hammingWeight(self, n):
        # inputs: n: int
        # outputs: int
        res = 0
        while n:
            n = n&(n-1)
            res += 1
        return res