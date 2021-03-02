# 题意：数组中数字出现次数2.在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
# 题解1: 用位运算，所有位的1的个数能被3整除，除非非重复数在该位上是1
# 题解2: 用有限状态机。有限状态机的思想也和位运算差不多，但写起来更为简单。
# 若统计每位上所有数的1的次数取余3，结果只会有0，1，2三种。我们可以 对每一位 建立状态机：
# 余数0-----余数1-----余数2，若该位是0则在此状态不动，若该位位1则变为余数+1的状态
# 状态机有三个状态要用两个比特来描述，故用two和one，然后找规律计算one two和item的关系来表达one和two。
# 这是每一位的，因为^ & ~都是按位操作所以对一个数也是这样。因为只有3个重复和1个不重复，所以其实只可能余数是0或1. one为1的话余数1那么就说明该位置存在，one为0说明该位置是能被三整除为0即可,最后我们看one就行

class Solution:
    def singleNumber(self, nums):
        # inputs: nums: List[int]
        # outputs: int
        # 按bit
        res = 0
        for i in range(32):
            b = 1 << i
            cnt = 0
            for item in nums:
                if item & b:
                    cnt += 1
            if cnt % 3 != 0:
                res |= b
        return (res-2**32) if res>(2**32-1) else res


class Solution_2:
    def singleNumber(self, nums):
        # inputs: nums: List[int]
        # outputs: int
        # 用有限状态机
        two, one = 0,0
        for item in nums:
            one = one ^ item & ~two
            two = two ^ item & ~one
        return one # 遍历完所有数字后，各二进制位都处于状态00和状态01（取决于“只出现一次的数字”的各二进制位是1还是0），而此两状态是由 one来记录的（此两状态下two恒为0），因此返回ones即可。