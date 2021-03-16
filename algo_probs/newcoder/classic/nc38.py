# 题意：螺旋矩阵输出，顺时针打印矩阵问题
# 题解：模拟法，注意边界即可
# 
# @param matrix int整型二维数组 
# @return int整型一维数组
#
class Solution:
    def spiralOrder(self , matrix ):
        # write code here
        if not matrix: return []
        res = []
        row,col = len(matrix),len(matrix[0])
        left,right,top,bottom = 0,col-1,0,row-1
        #i,j = 0,0
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1 
            if top>bottom: break
            for j in range(top,bottom+1):
                res.append(matrix[j][right])
            right-=1
            if right<left: break
            for k in range(right,left-1,-1):
                res.append(matrix[bottom][k])
            bottom-=1
            if bottom<top: break
            for l in range(bottom,top-1,-1):
                res.append(matrix[l][left])
            left+=1
            if left>right: break
        return res