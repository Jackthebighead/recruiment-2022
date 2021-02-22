# 题意：连续子数组的最大和问题。
# 题解1: linear time algorithm
# 本质是贪心算法，用一个max记录全局最大值，用一个cur记录当前最大。由于若当前的和小于0，后面无论加上什么都会小于原来的数，所以当cur<0是需要变为cur=0，在过程中遇见比max大的cur更新max即可。
# 题解2: 动态规划
# 维护一个dp数组，dp[i]代表以i结尾的最大数组和，状态转移方程很好写，这题是dp的基础题

class Solution:
    def maxSubArray(self, nums):
        # inputs: nums:List[int] 
        # outputs: int
        # linear time algorithm
        # 如果前面的和是负数，那么后面的部分和没必要加上前面
        max_sum,cur_sum = -101,0
        for item in nums:
            cur_sum += item
            if max_sum<cur_sum:
                max_sum = cur_sum
            if cur_sum<=0:
                cur_sum = 0
        return max_sum
                
class Solution_2:
    def maxSubArray(self, nums):
        # inputs: nums:List[int] 
        # outputs: int
        # 动态规划
        # 状态转移方程：
        # dp[i] = dp[i-1] + nums[i] if dp[i-1]>=0
        # dp[i] = nums[i] if dp[i-1]<0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        return max(dp)