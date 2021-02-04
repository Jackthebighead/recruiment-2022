# Binary Search
# input: target:int, data:list
# output: index: int
class bsearch():
    def go(self, target, data):
        if not target or not data:
            return -1
        
        l = 0
        r = len(data)
        while l<=r:
            mid = l + (r-l) // 2
            if data[mid] == target:
                return mid
            elif data[mid] < target:
                r = mid + 1
            else: 
                l = mid - 1
        return -1

sol = bsearch()
target = 1
data = [1,2,3,4,5]
print(sol.go(target,data))