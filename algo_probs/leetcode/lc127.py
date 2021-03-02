# 题意：只出现一次的数字，给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。用O(1)空间复杂度实现
# 题解：用位运算

class Solution:
    def singleNumber(self, nums):
        # inputs: nums: List[int]
        # outputs: int
        res = 0
        for i in range(32):
            b,cnt = 1,0
            b <<= i
            for item in nums:
                if item & b:
                    cnt += 1
            if cnt % 3 != 0:
                res |= b
        return res - 2 ** 32 if res > 2 ** 31 - 1 else res  # 因为python是动态语言最高位会被识别为而不是符号位