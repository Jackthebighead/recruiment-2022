# 题意：写一个函数 StrToInt，实现把字符串转换成整数这个功能
# 题解：直接写。注意边界
# 知识点：为数字的字符串大小 ord(char)-ord('0')，越界处理：32位数字的范围[2^32-1,-2^32]，2^32-1末尾是7
class Solution:
    def strToInt(self, str):
        # inpus: str: str
        # outputs: int
        str = str.strip(' ')
        if not str: return 0
        res,flag,i = 0,1,1
        int_max, int_min, boundary = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        if str[0] == '-': flag=-1  
        elif str[0] != '+': i = 0
        for char in str[i:]:
            if not ord('0')<=ord(char)<=ord('9'): break
            if res>boundary or (res==boundary and char>'7'):
                return int_max if flag==1 else int_min
            res = 10*res + ord(char)-ord('0')
        return flag*res
