# 题意：输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
# 题解1:暴力。。
# 题解2:大数越界问题： 当n较大时，end会超出int32整型的取值范围，超出取值范围的数字无法正常存储。

class Solution:
    def printNumbers(self, n):
        l = list(range(1,10**n))
        return l

