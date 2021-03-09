# 题意：找最小k个数，最大第k数
# 题解：快排变种

class Solution:
    def quicksort_with_pruning(self,tinput,l,r):
            i,j = l,r
            while i<j:
                while i<j and tinput[j]>=tinput[l]: j-=1
                while i<j and tinput[i]<=tinput[l]: i+=1
                tinput[i],tinput[j] = tinput[j],tinput[i]
            tinput[l],tinput[j] = tinput[j],tinput[l]
            return j
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k>len(tinput) or not tinput: return []
        # 快排+剪枝
        def recur(tinput,l,r):
            index = self.quicksort_with_pruning(tinput, l, r)
            if index == k-1: return sorted(tinput[:k])
            elif index > k-1: return recur(tinput,l,index-1)
            else: return recur(tinput,index+1,r)
        return recur(tinput,0,len(tinput)-1)


class Solution_2:
    def quicksort(self, data, l, r):
        #if l>=r: return
        i,j = l,r
        while i<j:
            while i<j and data[j]>=data[l]: j-=1
            while i<j and data[i]<=data[l]: i+=1
            data[i],data[j] = data[j],data[i]
        data[l],data[j] = data[j],data[l]
        return j
    def findKth(self, a, n, K):
        # write code here
        #if not a or K>n or K<=0: return -1
        def recur(data,l,r):
            index = self.quicksort(data, l, r)
            if index == n-K: return data[index]
            elif index > n-K: return recur(data,l,index-1)
            else: return recur(data,index+1,r)
        return recur(a,0,n-1)
        