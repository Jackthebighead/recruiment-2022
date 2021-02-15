# 题目：找出数组中任意一个有重复的数字
# 解法1：用hash O(n),O(n)
# 解法2：先sort再linear查找 O(nlogn),O(1)
# 解法3：原地置换，节省空间复杂度，依赖题意：n个数，数字在n-1范围内。循环这个list，如果index和value不一样，和value作为index的值比较，若一样返回，不一样一直交换直到index和value一样，进行循环下一步。

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

 # 解法2   
def findRepeatNumber_2(self, nums):
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

# 解法3
def findRepeatNumber_3(self, nums):
        # input: nums: List[int]
        # output: int
        for index, num in enumerate(nums):
            while index != num:
                if nums[num] == num:
                    return num
                else: 
                    num[num], num = num, nums[num]
    
