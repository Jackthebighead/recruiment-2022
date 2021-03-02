# 题意：字符串左旋转问题。字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。
# 题解：用切片，不能切片用list，不能用join用str遍历
class Solution:
    def reverseLeftWords(self, s, n):
        # inputs: s: str, n: int
        # outputs: str
        return s[n:]+s[:n]