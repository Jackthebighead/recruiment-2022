# 题意：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。你可以按任意顺序返回答案。

# 解法1: 暴力，用python的list实现查找，遍历一次list，若target和当前值的差在list余下中，则返回。
# 解法2: 哈希列表。其实和思路1差不多，在python中用dict来实现，每次循环查找target-i是否在dict中，若在则返回，不在就添加。

class Solution:
    def twoSum(self, nums, target):
        # input: nums: List[int], target: int
        # output: List[int]
        for i,item in enumerate(nums):
            if target-item in nums[i+1:]:
                return [i,nums[i+1:].index(target-item)+i+1]
        return


class Solution_2:
    def twoSum(self, nums, target):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []