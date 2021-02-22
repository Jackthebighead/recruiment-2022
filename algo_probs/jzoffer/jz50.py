# 题意：第一个只出现一次的字符
# 题解1: 维护一个有序字典：key，value为字符和出现次数，然后遍历字典找出第一个value为1的key，返回。
# 优化：value为boolean就行不需要次数，dict用dict就行因为3.6之后已经有序

class Solution:
    def firstUniqChar(self, s):
        # inputs: s: str
        # outputs: str
        if not s:
            return ' '
        import collections
        d = collections.OrderedDict()
        n = len(s)
        for i in range(n):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        for i,j in d.items():
            if j == 1:
                return str(i)
        return ' '