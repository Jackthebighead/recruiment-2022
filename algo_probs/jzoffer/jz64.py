# 题意：求1到n的和。求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
# 题解：用短路的方法。当表达式为A and B时，只要A为假直接判定为假俺么B即递归就会终止。再用一个类变量self.res来记录加和即可。

class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n):
        # inputs: n: int
        # outputs: int
        n>1 and self.sumNums(n-1)
        self.res += n
        return self.res