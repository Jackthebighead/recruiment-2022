# 题意：给你一个字符串 s，找到 s 中最长的回文子串。
# 题解1: 中心扩散法：依次遍历每一个字符，以每个字符为中心向外延展直到不是回文，保留最长的回文index，返回回文串。需要另外注意两个问题，回文中心是一个字符还是两个字符（奇数偶数）问题，分开讨论。
# 题解2: 动态规划：首先明确题目求最长回文子串，因若s[i:j]是子串那么s[i-1,j+1]也是子串，将动态规划的状态设为i：j是否为回文子串，初始化一个n*n的二维数组，遍历的顺序为回文串长度（用长度来讨论更好）为1-n，
# 首字母为1-n，对长度为1和2的讨论（奇偶问题），其他的由状态方程决定，每次判断是否为最长，若最长保留即可。
 

class Solution:
    def cal_hwc(self, s, start, end):
        while start>=0 and end<len(s) and s[start]==s[end]:
            start -= 1
            end += 1
        return start+1, end-1
            
    def longestPalindrome(self, s):
        # inputs: s: str
        # outputs: str
        best_start, best_end, n= 0,0,len(s)
        for p in range(n):
            start_1, end_1 = self.cal_hwc(s, p, p)
            start_2, end_2 = self.cal_hwc(s, p, p+1)
            if end_1 - start_1 > best_end - best_start:
                best_start, best_end = start_1, end_1
            if end_2 - start_2 > best_end - best_start:
                best_start, best_end = start_2, end_2
        return s[best_start:best_end+1]

class Solution_2:
    def longestPalindrome(self, s):
        # inputs: s: str
        # outputs: str
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ''
        for l in range(n):
            for i in range(n):
                j = i + l
                if j>=n:
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    if s[i]==s[j]:
                        dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i]==s[j]
                if dp[i][j] and l+1>len(res):
                    res = s[i:j+1]
        return res




