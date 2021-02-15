# 题意：请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。
# 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
# 题解：动态规划。🤯

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # inputs: s: str, p: str. s是用例，p是模式
        # outputs: bool
        # 定义匹配函数，函数要考虑'.'正则匹配的情形
        def match(i,j):
            if i == 0:
                return False
            if p[j-1] == '.':
                return True
            else:
                return s[i-1]==p[j-1]
        # 开始匹配
        # 初始化：建立一个全是flase的dp矩阵，初始化0，0（空字符串匹配空字符串）为0
        n,m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]  
        dp[0][0] = True
        for i in range(n+1):
            for j in range(1,m+1):
                # 对每个s字符，用整个p进行匹配
                # 第一种情况，当有模式对应的是*时，有两种可能，
                # 若当前用例字符和前一个模式字符匹配，比如用例a，模式是a*，那么模式的a允许*前有0或无数个a，那么d[i][j]取决于i和j-2（有0个a的情况）或i-1和j（有多个a的情况，上一个用例字符是否也是模式）
                # 若不匹配，只可能是有0个a的情形
                # 第二种情况，当模式不是*的时候，简单，就是若匹配，返回dp[i-1][j-1]，若不匹配false
                # 用|=代表或等于
                if p[j-1] == '*':
                    dp[i][j] |= dp[i][j-2]
                    if match(i,j-1):
                        dp[i][j] |= dp[i-1][j]
                else:
                    if match(i,j):
                        dp[i][j] |= dp[i-1][j-1]
                    #else:  # 本身就是false这里就没必要讨论了
                    #    df[i][j] = False
        return dp[-1][-1]
                    







        