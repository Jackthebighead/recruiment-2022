# 题意： 下一个最大元素问题：给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
# 题解：单调栈
# https://leetcode-cn.com/circle/discuss/kdY0zV/

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # inputs: nums1: List[int], nums2: List[int]
        # outputs: List[int]
        if not nums1 or not nums2:
            return 
        # 由于nums1是nums2的一个子集，所以只需对nums2操作。实现一个从左到右的单调递减栈即可
        n,stack = len(nums2),[]
        dt = {}
        for i in range(n):
            while stack and nums2[i]>stack[-1]:  # nums2[i]: new
                dt[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        return [dt.get(x,-1) for x in nums1]
            

