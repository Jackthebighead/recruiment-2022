# 青蛙跳台阶
# 递归可以但要考虑时空复杂度
# 用这样的方法
# 或存放到数组中
class Solution:
    def jumpFloor(self, number):
        # write code here
        a=0
        b=1
        for _ in range(number+1):
            a,b = a+b,a
        return a