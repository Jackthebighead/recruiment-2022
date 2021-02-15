# 题意：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
# 题解：这道题实际上需要运用状态机的思想，根据字符类型和合法数值的特点，先定义状态，再画出状态转移图，最后编写代码即可。代码中状态用字典列表，列表中每个字典是每个状态，每个字典里的所有key是该状态下可做的动作，value是动作导致的下一个状态。有点类似于穷举法把。  
# 这题可以列出‘+5.12e-3’这样相对最复杂的情形来分析，首先需要考虑开头和结尾有空格，所以所有的动作有：‘ ’，‘数字’，‘正负号’，‘指数eE’，‘小数点’。
# 至于状态，举个例子，开始是空格的话下一个字符也可能是空格，或者正负号，或者数字，或者小数点，根据这四种情形可以将状态0通过这些动作连接到其他不同的状态，依次类推。
# 题解2: 用python的trick即float以及try and except

class Solution:
    def isNumber(self, s):
        # inputs: s: str
        # outputs: bool
        # 先定义状态转换字典，state[p][t]，p代表状态，t代表该状态下可选动作
        states = [
            {' ':0, 's':1, 'd':2, '.':4},  # state:0
            {'d':2, '.':4},  # state:1
            {'d':2, '.':3, 'e':5, ' ':8},  # state:2
            {'d':3, 'e':5, ' ':8},  # state:3
            {'d':3},  # state:4 这个单独拎出来是因为存在.3这样小数点前没有符号和数字的情况，4接3的状态
            {'s':6, 'd':7}, # state:5
            {'d':7}, # state:6
            {'d':7, ' ':8}, # state:7
            {' ':8} # state:8
        ]
        p = 0
        # 遍历字符串s
        for c in s:
            if '0'<= c <='9':
                t = 'd'
            elif c in '+-':
                t = 's'
            elif c in ' ':
                t = ' '
            elif c in '.':
                t = '.'
            elif c in 'eE':
                t = 'e'
            else:
                t = '?'  # unknown

            if t not in states[p]: 
                return False
            p = states[p][t]
        return p in (2,3,7,8)


class Solution_2:
    def isNumber(self, s):
        # inputs: s: str
        # outputs: bool
        try:
            res = float(s)
            return True
        except ValueError:
            return False

        







