class Solution:
    def quicksort(self, arr, l, r):
        if l>=r: return 
        i,j = l,r
        while i<j:
            while i<j and arr[j]>=arr[l]:
                j-=1
            while i<j and arr[i]<=arr[l]:
                i+=1
            arr[i],arr[j] = arr[j],arr[i]
        arr[l],arr[j] = arr[j],arr[l]
        self.quicksort(arr,l,j-1)
        self.quicksort(arr,j+1,r)
    def MySort(self, arr):
        # write code here
        # quick sort solution
        self.quicksort(arr,0,len(arr)-1)
        return arr