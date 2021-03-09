# 题意：合并两个有序数组  错题❌！！！！！
# 题解1: sort
# 题解2: 不能开辟新空间，所以从后往前merge

# @param A int整型一维数组 
# @param B int整型一维数组 
# @return void
#
class Solution:
    def merge(self , A, m, B, n):
        # write code here
        # 因为不能开辟新空间，所以从后往前放
#         if not A: return B
#         if not B: return A
#         if not A and not B: return []
        A[m:] = B
        return A.sort()  # 因为不能返回新的list所以用.sort()

class Solution_2:
    def merge(self , A, m, B, n):
        # write code here
        # 因为不能开辟新空间，所以从后往前放
        if m==0: 
            A[:] = B[:]
        i,j = m-1,n-1
        while i>=0 and j>=0:
            if A[i]>=B[j]:
                A[i+j+1] = A[i]
                i-=1
            else:
                A[i+j+1] = B[j]
                j-=1
        if i<0: A[:j+1] = B[:j+1]
