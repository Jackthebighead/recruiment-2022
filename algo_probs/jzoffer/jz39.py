# 题意：众数。数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 题解1: 用哈希方法，设置一个字典，然后变成找字典中值最大的键，用max函数和lambda自定义过滤。
# 题解2: 用linear time algorithm
# 题解3: 用sorted之后的中位数

class Solution:
    def majorityElement(self, nums):
        # inputs: nums: List[int]
        # outputs: int
        # linear time algorithm
        # hash
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 0
        return max(d,key=lambda x:d[x])
        # return max(d,d.get)
        # a = max(d.items(),key=operator.itemgetter(1))
        # print(a[0])

class Solution_2:
    def majorityElement(self, nums):
        # inputs: nums: List[int]
        # outputs: int
        # linear time algorithm
        if not nums:
            return 
        n,major,cnt = len(nums),nums[0],1
        for i in range(1,n):
            # 众数规律：若为众数投票+1，不为-1，则投票为0时，剩余list中的众数不变且最终众数投票>0。因为众数的个数大于一半，所以可以抵消。
            if cnt == 0:
                major = nums[i]
                cnt = 1
            elif major != nums[i]:
                cnt -= 1
            else:
                cnt += 1
        return major

class Solution_3:
    def majorityElement(self, nums):
        # inputs: nums: List[int]
        # outputs: int
        # hacky way
        return sorted(nums)[int(len(nums)/2)]
