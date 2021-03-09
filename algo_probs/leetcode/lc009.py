# 题意：回文数
# 题解1: 转换成字符串，然后用首尾双指针回溯
# 题解2: 分类讨论，负数不行，0-9可以，两位数及以上若为回文则倒序和自身相等。
# 题解3: 取后半段数字反转

class Solution:
    def isPalindrome(self, x):
        x = str(x)
        l,r = 0,len(x)-1
        while l<r and x[l]==x[r]: l,r = l+1,r-1
        return l>=r

class Solution_2:
    def isPalindrome(self, x):
        if x<0: return False
        if 0<=x<=9: return True
        xx,res = x,[]
        while xx: 
            res.append(xx%10)
            xx //= 10
        x_c = 0
        for i in res:
            x_c = x_c*10 + i
        return x_c == x