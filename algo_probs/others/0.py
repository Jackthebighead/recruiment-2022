# 题意：实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
# 题解1: set
# 题解2: 位运算。这里假设题目只涉及到26个字母。我们可以用一个mask，把它看作二进制，第i位记录第i个字母是否出现过。比如字母b若出现过，mask则或运算1<<(ord('b')-ord('a'))，即可，遍历数组，若mask和当前1<<(ord('b')-ord('a'))想与不为0即该位置已为1，那么返回False说明有重复。

class Solution:
    def isUnique(self, astr):
        return len(set(astr))==len(astr)

class Solution_2:
    def isUnique(self, astr):
        mask = 0 
        for item in astr:
            # 若astr里面只属于二十六个字母
            if mask & (1<<(ord(item)-ord('a'))) !=0:
                return False
            mask |= (1<<(ord(item)-ord('a')))
        return True