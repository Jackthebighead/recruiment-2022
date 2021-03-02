# 题意：滑动窗口最大值问题。给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
# 题解1: 暴力方法依次遍历，求区间最大值。可以用双指针来控制窗口
# 题解2: 线性时间方法，用一个递减双端队列来记录最大值。分类讨论：当窗口小于k，当窗口大于k开始滑动。前者，队列只保留最大数，后者，当队头元素等于滑动窗口此时要舍弃的数则pop，对进入窗口的数维护递减队列，不满足递减的全pop。

class Solution:
    def maxSlidingWindow(self, nums, k):
        # inputs: nums: List[int], k: int
        # outputs: List[int]
        # minus left value and add right value
        if not nums:
            return []
        if k>len(nums):
            return max(nums)
        res = [max(nums[0:0+k])]
        l,r = 0,0+k-1
        while r<len(nums)-1:
            l += 1
            r += 1
            res.append(max(nums[l:r+1]))
        return res

class Solution_2:
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0: return []
        import collections
        deque = collections.deque()
        for i in range(k): # 未形成窗口
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        for i in range(k, len(nums)): # 形成窗口后
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res
