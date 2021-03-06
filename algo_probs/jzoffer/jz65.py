# 题意：不用加减乘除的加法：写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
# 题解：不能四则运算只能位运算了
# 两个数字的二进制相加，11位0且进位，10或01为1且不进位，00为0，故可以分为进位和不进位两种：又因为进位要往前一位+1，所以进位为x&y<<1；不进位为: x^y异或以下即可。相加可以转换为进位加和与不进位加和相加。
# 但仍无法相加，我们可以考虑迭代求这两个，即进位加和与不进位加和为新的两个加数。直到没有进位，那么最后结果就是前者了。
# 剩下就要解决python中数据存储问题，python无位数限制且以补码存储0xffffffff会被判断成498987597而不是-1。故我们要将负数符号考虑进来的话得加个判断。先限制位数，再带入迭代式计算（此时因为进行位运算故不用担心是否会被判断成错误的数的问题，只有出口的时候需要判断，且也不用担心溢出）

class Solution:
    def add(self, a: int, b: int) -> int:
        # inputs: a: int, b: int
        # outputs: int
        mask = 0xffffffff
        a,b = a&mask,b&mask
        while b!=0:  # b==0时convergence
            a,b = a^b,(a&b)<<1 & mask  # 分别位不进位部分和进位部分，进位部分要&以下mask的意义是当最高位为1和1的时候会移位到第33位，这时候要消除掉，因为a^b对于1和1的话还是1，保留负数符号，所以直接消除即可。
        return a if a<=0x7fffffff else ~(a^mask)  # 对正数和负数判断