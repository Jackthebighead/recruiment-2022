# 题意：给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列。括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。

# @param s string字符串 
# @return bool布尔型
#
class Solution:
    def isValid(self , s ):
        # write code here
        if not s: return True
        stack = []
        dic = {'{':'}','[':']','(':')'}
        for char in s:
            if not stack or char in dic: stack.append(char)
            elif stack and dic.get(stack[-1])!=char: return False
            else:
                stack.pop()
                continue
        return True
               