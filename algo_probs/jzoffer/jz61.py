# 题意：扑克牌中的顺子。从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
# 题解：用set保存即可set的查找为O(1)

class Solution:
    def isStraight(self, nums):
        # inputs: nums: List[int]
        # outputs: bool
        poke, mi, ma = set(),0,14
        for num in nums:
            if num == 0: continue
            if num in poke: return False
            ma = min(num, ma)
            mi = max(num, mi)
            poke.add(num)
        return mi-ma<5 
