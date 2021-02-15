# 题意：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。即蛇形输出
# 题解1：模拟法，主要考虑各种边界情况。。degbug。。 
# 题解2: 用python的特性，重复：输出第一行，删掉第一行（加入result），翻转。 matrix是由list中list组成，pop(0)输出第一行，然后将matrix按行zip起来倒序，就等于将矩阵向左翻转90度，再pop删掉，重复操作即可。

class Solution:
    def spiralOrder(self, matrix):
        # inputs: matrix: List[List[int]]
        # outputs: List[int]
        if not matrix:
            return []
        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)
        res = []
        while True:
            # 从左到右
            for i in range(l,r):
                res.append(matrix[t][i])
            t += 1
            if t>=b: break

            # 从上到下
            for j in range(t,b):
                res.append(matrix[j][r-1])
            r -= 1
            if l>=r: break
            
            # 从右到左
            for k in range(r-1,l-1,-1):
                res.append(matrix[b-1][k])
            b -= 1
            if t>=b: break

            # 从下到上
            for q in range(b-1,t-1,-1):
                res.append(matrix[q][l])
            l += 1
            if l>=r: break

        return res
            
            
class Solution_2:
    def spiralOrder(self, matrix):
        # inputs: matrix: List[List[int]]
        # outputs: List[int]
        if not matrix:
            return []
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res 
            
            
                
             
