# 题意：找出和为s的两个数字，输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
# 题解：双指针对撞，因为是递增序列，若和大于target则右指针要减少，否则左指针要增加

class Solution:
    def twoSum(self, nums, target):
        # inputs: List[int], target: int
        # outputs: List[int]
        l,r = 0,len(nums)-1
        while l<r:
            s = nums[l] + nums[r]
            if s == target: return [nums[l],nums[r]]
            elif s>target: r -= 1
            else: l += 1
        return []
