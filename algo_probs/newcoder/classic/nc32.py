# 题意：实现求平方根的函数
# 题解：二分法。注意边界条件。由于是向下取整，且二分中若mid*mid大于x，right=mid-1，此时right为最小值；若mid*mid小于x，left=mid+1，此时right仍为最小值。所以返回right
# 
# @param x int整型 
# @return int整型
#
class Solution:
    def sqrt(self , x ):
        # write code here
        if x<0: return -1
        if x<=1: return x
        left,right = 0,x
        while left<=right:
            mid = left+(right-left)//2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                right = mid-1
            else: left = mid + 1
        return right