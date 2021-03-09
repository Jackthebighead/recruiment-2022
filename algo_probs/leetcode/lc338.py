# 题意：比特位计数。给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。要求用O(n)的时间复杂度
# 题解：若要求linear time，观察规律，发现：若位奇数，1的个数是前一个偶数的1个数加1（因为前一个偶数最低位必位0），偶数和它除以2的偶数的个数相同。

class Solution:
    def countBits(self, num):
        # inputs: num: int
        # outputs: List[int]
        res = []
        for i in range(num+1):
            if i == 0:
                res.append(0)
            elif i == 1:
                res.append(1)
            elif i % 2: 
                res.append(res[i-1]+1)
            else:
                res.append(res[i//2])
        return res


