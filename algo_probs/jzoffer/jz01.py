# 题目：找出数组中任意一个有重复的数字
# 解法1：用hash O(n),O(n)
# 解法2：先sort再linear查找 O(nlogn),O(1)
# 解法3：原地置换，节省空间复杂度，依赖题意：n个数，数字在n-1范围内
class Solution:
    def findRepeatNumber(self, nums):
        # input: nums: List[int]
        # output: int
        res_dict = dict()
        for i in nums:
            if res_dict.get(i) is not None:
                return i
            else: res_dict[i] = i
        return 

sol = Solution()
print(sol.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))

class Solution_2:
    def findRepeatNumber(self, nums):
        # input: nums: List[int]
        # output: int
        nums.sort()
        pre = None  # 上一个数字
        for i in nums:
            if i == pre: 
                return i
            else: 
                pre = i
        return

class Solution_3:
    def findRepeatNumber(self, nums):
        # input: nums: List[int]
        # output: int
        for index, num in enumerate(nums):
            while index != num:
                if nums[num] == num:
                    return num
                else: 
                    num[num], num = num, nums[num]

