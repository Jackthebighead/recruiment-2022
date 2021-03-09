# 题意 两数之和
class Solution:

    def twoSum(self , numbers , target ):
        # write code here
        if not numbers: return []
        d = {}
        for i,num in enumerate(numbers):
            if target-num in d:
                return [d.get(target-num),i+1]
            else:
                d[num] = i+1
        return []