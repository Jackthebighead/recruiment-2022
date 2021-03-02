# 题意：topk问题
# 题解1: 先排序后返回
# 题解2: 堆排序，或nlargest
# 题解3: 快排，再返回
# 题解4: 快速选择算法，在排的过程中只返回有前k数字的那一边。是最优解法，时间O(n)空间O(lgN)因为递归要用栈
# 快速选择算法主要是用于在未排序的数组中找到第 k 个最小/大数字的算法

class Solution:
    def getLeastNumbers(self, arr, k):
        # inputs: arr: List[int], k: int
        # outputs: List[int]
        res = []
        arr = sorted(arr,reverse=True)
        for _ in range(k):
            res.append(arr.pop())
        return res

class Solution_2:
    def getLeastNumbers(self, arr, k):
        # inputs: arr: List[int], k: int
        # outputs: List[int]
        import heapq
        heapq.heapify(arr)  # 将一个list变成heap
        return [heapq.heappop(arr) for _ in range(k)]  # heapq.heappop(list)弹出最小值

class Solution_3:
    def getLeastNumbers(self, arr, k):
        # inputs: arr: List[int], k: int
        # outputs: List[int]
        def quick_sort(data, l, r):
            if l>=r: return 
            i,j = l,r
            while i<j:
                while i<j and data[i]<=data[l]: i += 1
                while i<j and data[j]>=data[l]: j-= 1
            data[i],data[j] = data[j],data[i]
            data[l],data[i] = data[i],data[l]
            # 现在j是pivot的位置
            # 以下是递归，递归尽头是l>=r
            quick_sort(data,l,j-1)
            quick_sort(data,j+1,r)
        
        quick_sort(arr,0,len(arr)-1)
        return arr[:k]

class Solution_4:
    def getLeastNumbers(self, arr, k):
        # inputs: arr: List[int], k: int
        # outputs: List[int]
        def quick_sort(data, l, r):
            if l>=r: return 
            i,j = l,r
            while i<j:
                while i<j and data[i]<=data[l]: i += 1
                while i<j and data[j]>=data[l]: j-= 1
            data[i],data[j] = data[j],data[i]
            data[l],data[i] = data[i],data[l]
            # 现在j是pivot的位置
            # 以下是递归，递归尽头是l>=r
            if i>k: quick_sort(data,l,i-1)
            if i<k: quick_sort(data,i+1,r)
            return data[:k]
        return quick_sort(arr,0,len(arr)-1)




