# 题意：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
# 双指针问题
# 题解1: 使用快慢指针，首先找到第一个偶数，然后慢指针从这开始，快指针从慢指针下一位开始遍历直到找到奇数（偶数后面的奇数）为止，此时交换，快慢指针各+1（慢指针可以+1是因为慢指针之后至少有一个偶数（换过去的，或下一个偶数））。
# 要考虑各种边界。
# 题解2：使用左右双指针，从左到右从右到左，左为偶数右为奇数则交换。


class Solution:
    def exchange(self, nums):
        # inputs: List[int]
        # outputs: List[int]
        if not nums:
            return nums
        a,b,n = 0,0,len(nums) # a: odd, b: even
        if n == 1:
            return nums
        # a跳到偶数位
        for i in range(n):
            if nums[i]%2 == 0:
                a = i
                break
            if i == n-1:
                return nums
        b = a+1
        while b<n:
            # b跳到奇数位，换
            if nums[b]%2 == 1:
                nums[a], nums[b] = nums[b], nums[a]
                a,b = a+1, b+1
            # 若num[b]为偶数一直跳下去
            else:
                b = b + 1
        return nums

class Solution_2:
    def exchange(self, nums):
        # inputs: List[int]
        # outputs: List[int]
        left, right = 0,len(nums)-1
        while left<right:
            while nums[left]%2!=0 and left<right:
                left += 1
            while nums[right]%2==0 and left<right:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left+1, right-1
        return nums