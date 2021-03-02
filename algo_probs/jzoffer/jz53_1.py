# 题意：在排序数组中查找数字。统计一个数字在排序数组中出现的次数
# 题解1: 暴力，直接遍历
# 题解2: 左右双指针往回遍历
# 题解3: 二分法，注意当mid等于target的时候要往左右递归，递归函数返回一个计数，满足就不断+1。该二分法递归等于target的计数
# 题解4: 也是二分法，但是二分法的目的是找出左右两个为target的边界，最后返回r-l+1. 优化是如果第一次没找到等于target的值可以直接退出避免第二次二分。也可以把两次二分写成一个函数。
# **题解4可以作为模版，主要在于等于mid的时候和合并到大于或小于的情形下**
# 题解5: list.count(target)

class Solution:
    def search(self, nums, target):
        # inputs: nums: List[int], target: int
        # outputs: int
        res = 0
        for i in nums:
            if i == target:
                res+= 1
        return res

class Solution_2:
    def search(self, nums, target):
        # inputs: nums: List[int], target: int
        # outputs: int
        l,r= 0,len(nums)-1
        if not nums or nums[l]>target or nums[r]<target:
            return 0
        while nums[l]<target:
            l += 1
        while nums[r]>target:
            r -= 1
        if l>r: return 0
        else: return r-l+1


class Solution_3:
    def search(self, nums, target):
        # inputs: nums: List[int], target: int
        # outputs: int
        # 二分法
        l,r = 0,len(nums)-1
        def recur(l,r,cnt):
            if l>r:
                return cnt
            mid = l + (r-l) // 2
            if nums[mid] == target:
                cnt += 1
                cnt = recur(l,mid-1,cnt)
                cnt = recur(mid+1,r,cnt)
            elif nums[mid] > target:
                cnt = recur(l,mid-1,cnt)
            else:
                cnt = recur(mid+1,r,cnt)
            return cnt
        return recur(l,r,0)


class Solution_4:
    def search(self, nums, target):
        # inputs: nums: List[int], target: int
        # outputs: int
        # 二分法
        l,r = 0,len(nums)-1
        if not nums or nums[l]>target or nums[r]<target:
            return 0
        # 先找左边界
        # left,right = 0,0
        while l<=r:
            mid = (l+r) // 2
            if nums[mid]>=target:
                r = mid-1
            else:
                l = mid+1
        left = r  # 此时r的位置是最左的一个target相等值的左边一位
        # 再找右边界，只需重新对r赋值
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r) // 2
            if nums[mid]<=target:
                l = mid+1
            else:
                r = mid-1
        right = l  # 此时l的位置是最右边的一个与target相等值的右边一位
        return right-left-1

class Solution_5:
    def search(self, nums, target):
        return nums.count(target)

