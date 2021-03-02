# 题意：一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
# 题解1: 位运算
# 题解2: 二分法，注意边界条件！

class Solution:
    def missingNumber(self, nums):
        # 位运算
        res = 0
        for i in range(len(nums)+1): res ^= i 
        for j in nums: res ^= j
        return res

class Solution_2:
    def missingNumber(self, nums):
        # 二分法
        l,r,res = 0,len(nums)-1,-1
        while l<=r:
            mid = l + (r-l) // 2
            if nums[mid] == mid:
                l = mid + 1 
            else:
                r = mid - 1        
        return l