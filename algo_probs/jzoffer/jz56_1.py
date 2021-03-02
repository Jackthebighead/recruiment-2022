# 题意；数组中数字出现的次数。一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
# 该题的关键是只要找出这两个数字即可
# 题解1: 暴力求解，但不符合空间复杂度
# 题解2: 本题的正确解：用位运算

class Solution:
    def singleNumbers(self, nums):
        # inputs: nums: List[int]
        # outputs: List[int] 
        res = {}
        for i in nums:
            if i in res:
                res.pop(i)
            else:
                res[i] = 0
        return list(res.keys())


class Solution_2:
    def singleNumbers(self, nums):
        # inputs: nums: List[int]
        # outputs: List[int] 
        import functools
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]