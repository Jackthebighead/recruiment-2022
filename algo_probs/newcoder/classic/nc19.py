# 题意：给定一个数组arr，返回子数组的最大累加和
# 题解：linear time solution

#
# max sum of the subarray
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxsumofSubarray(self , arr ):
        # write code here
        # linear time solution
        if not arr: return 0
        mx,cur_sum = 0,0
        for i in arr:
            cur_sum += i 
            if cur_sum > mx: mx = cur_sum
            if cur_sum < 0: cur_sum = 0
        return mx
