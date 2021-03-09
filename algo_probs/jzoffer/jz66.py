# 题意：构建乘积数组给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
# 题解：用两次遍历。第一次将顺着乘的中间结果赋值给对应res的i，第二次倒着乘。
# 想象1234，对res下标i，a[0]*...*a[i-1]是有用的，对于i+1，a[0]*...*a[i]是有用的，故可以将中间结果在依次遍历保存复用。
# 0： 2*3*4
# 1： 1*3*4
# 2： 1*2*4
# 3： 1*2*3

class Solution:
    def constructArr(self, a):
        # inputs: a: List[int]
        # outputs: List[int]
        res = [1 for _ in range(len(a))]
        temp = 1
        for i in range(1,len(a)):
            temp *= a[i-1]
            res[i] *= temp
        temp = 1
        for j in range(len(a)-2,-1,-1):
            temp *= a[j+1]
            res[j] *= temp
        return res