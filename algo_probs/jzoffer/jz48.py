# 题意：最长不含重复字符的子串问题。请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
# 题解1: 双指针（滑动窗口）+哈希。用哈希法维护一个key，value为字符，下标的字典。用右指针遍历字符串，遍历过程维护一个max length。
# 核心逻辑是：左指针位置为上一个重复的地方和这一个重复的地方的最大值，若这次重复的地方在上一次之前则忽略，直接用上一次的位置。
# 题解2: 动态规划+哈希：维护一个动态规划表。
# 注意此时动态规划转移方程不是p[j] = max(dp[j-1],j-i)，而是当dp[i-1]<j-i时即j字符出现在上一个最长子串之前的部分，则当前最长子串应该加一，dp[j]=dp[j-1]+1, 不然则dp[j] = j-i]。(i为j字符上一次出现的地方)
# 改进之处是直接维护一个全局最大值，不用建立dp表，节省空间复杂度。
# 题解3: 动态规划+线性查找，动态规划的dp[i]代表以i结尾的最长不重复子串。该方法最耗时间。

class Solution:
    def lengthOfLongestSubstring(self, s):
        # inputs: s: str
        # outputs: int
        # 双指针（滑动窗口）+哈希
        if not s:
            return 0
        d,i,res,n = {},-1,1,len(s)  # i，即左指针记录上一次重复的位置
        for j in range(n):
            if s[j] in d:  # 先写条件
                i = max(i,d[s[j]])  # 上一个重复的地方和这一个重复的地方的最大值，若这次重复的地方在上一次之前则忽略，直接用上一次的位置。
            d[s[j]] = j  
            res = max(res,j-i)  # 全局最大值和当前最长子串的比较
        return res


class Solution_2:
    def lengthOfLongestSubstring(self, s):
        # inputs: s: str
        # outputs: int
        # 动态规划+哈希
        if not s:
            return 0
        d, res, temp, n = {}, 0, 0, len(s)  # temp用来存dp[i-1]
        for j in range(n):
            i = d.get(s[j],-1)
            temp = temp + 1 if temp<j-i else j-i  # 若当前重复地方在上一循环的子串之前，则不管当前的i，直接temp+1因为这样才是当前最小子串，反之若在之后，则以j结尾的子串最大为j-i位置
            d[s[j]] = j
            res = max(res,temp)
        return res