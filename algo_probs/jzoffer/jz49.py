# 题意：我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
# 题解：动态规划

# 丑数的递推性质： 丑数只包含因子 2, 3, 5，因此有 “丑数=某较小丑数*某因子”。
# 合并 3 个有序序列， 最简单的方法就是每一个序列都各自维护一个指针， 然后比较指针指向的元素的值， 将最小的放入最终的合并数组中， 并将相应指针向后移动一个元素。 

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # inputs: n: int
        # outputs: int
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        p2,p3,p5 = 0,0,0  # 代表三个指针，分别代表当前丑数乘以2，3或5
        for i in range(1,n):
            # 当前丑数是p2，p3或p5代表的丑数分别乘以235的最小值。这里从dp[0]=1开始，可以乘2，乘3或乘5，若取了乘2的当dp[1]，那么dp[2](i)的候选就是dp[1](i-1)乘2，或之前结果中的两者（dp[0]*3或dp[1]*5）。动态规划求最小值，插入即可。
            # 也可以看成是所有丑数*2，*3和*5各为一个数列，然后从三个数列每次取最小值放入最终结果中。是一个合并三个有序数列的问题。
            dp[i] = min(min(dp[p2]*2,dp[p3]*3),dp[p5]*5) 
            # 不用if else而是用if是因为可能出现三个候选值重复的情况，若重复则都要移位
            if dp[i] == dp[p2]*2:
                p2 += 1
            if dp[i] == dp[p3]*3:
                p3 += 1
            if dp[i] == dp[p5]*5:
                p5 += 1
        return dp[-1]

