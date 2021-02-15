# 题意：替换字符
# 解法1：用list或str新建辅助结构遍历，遇见了就替换
# 解法2：直接用python的reverse函数

class Solution:
    def replace_space(self, s):
        s = s.replace(' ', '%20')
        return s

sol = Solution()
print(sol.replace_space('We are happy'))

class Solution_2:
    def replace_space(self, s):
        res = ''
        for i in list(s):
            if i == ' ':
                res += '%20'
            else: 
                res += i
        return res

sol = Solution_2()
print(sol.replace_space('We are happy'))


class Solution_3:
    def replace_space(self, s):
     # 注意了解列表转成字符串方法：''.join(res)，使用join函数```
        res = []
        for i in s:
            if i == ' ':
                res.append('%20')
            else: 
                res.append(i)
        return ''.join(res)

sol = Solution_3()
print(sol.replace_space('We are happy'))