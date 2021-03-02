# 题意：
# 题解1: 暴力+滑动窗口：从每一个点以每一个滑动窗口来遍历，注意剪枝不然会超时
# 题解2: 双指针。指针间的区间为candidate，若candidate的和大于target则左边界+1，若小于则右边界+1.比题解1快得多。

class Solution:
    def findContinuousSequence(self, target):
        # inputs: target: int
        # outputs: List[List[int]]
        # 想用滑动窗口
        res = []
        for i in range(1,target):  #  遍历整个数组
            for j in range(2,target-i):  # 遍历所有长度的窗口
                if i+j-1<target and sum(list(range(i,i+j)))==target:
                    res.append(list(range(i,i+j)))
                if sum(list(range(i,i+j)))>target: break
        return res
                
class Solution_2:
    def findContinuousSequence(self, target):
        # inputs: target: int
        # outputs: List[List[int]]
        # 改进版双指针（滑动窗口）
        i,j,s,res = 1,2,3,[]
        while i<j:
            if s == target: res.append(list(range(i,j+1)))
            if s < target:
                j += 1
                s += j
            else:
                s -= i
                i += 1
        return res


                