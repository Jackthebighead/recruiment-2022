# 题意：有重复数据的二分查找

class Solution:
    def search(self , nums , target ):
        # write code here
        # 若有重复找最左边的数字
        if not nums or target<nums[0] or target>nums[len(nums)-1]:
            return -1
        l,r = 0,len(nums)
        while l<r:
            mid = l+(r-l)//2
            if nums[mid] >= target: r = mid
            else: l = mid+1
        return r if nums[r]==target else -1
