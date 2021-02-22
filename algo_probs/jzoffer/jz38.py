# 题意：输入一个字符串，打印出该字符串中字符的所有排列。
# 题解1: 本题经典。考察深度遍历+回溯（剪枝）。关键在于用set存储重复数字
# 题解2: 全排列方法，先sorted再用类似的回溯+深度遍历。因为sort来所以用i与i-1比较即可找出是否重复。

# dfs回溯模版？：
# def dfs(status):
#     if boundary:
#         operation()
#         return sth
#     for i in all_cases:
#         if i satisfies pruning rule:
#             continue  # pruning
#         do sth()
#         dfs(next_status)
#         redo sth  # backtracking as i will be increased in the loop

# 字符串回溯法全排列模版？：
def permutation_str(s:str):
    if not s: return 
    def dfs(s,temp):
        # boundary
        if not s:
            res.append(''.join(temp))
            return 
        for i,char in enumerate(s):
            if i>0 and s[i] == s[i-1]:  # 注意得有i>0
                continue
            # do nothing
            dfs(s[:i]+s[i+1:],temp+char)
            # redo nothing
    res = []
    s = list(sorted(s))  # sort的作用就是我们只需要判定s[i]与s[i_1]是否重复即可
    dfs(s,[])
    return res

# 列表全排列模版？：
def permutation_list(l:list):
    if not l: return 
    def dfs(l, temp):
        # boundary:
        if not s: res.append(temp)
        for i in range(len(l)):
            if i>0 and l[i]==l[i-1]:  # 注意得有i>0
                continue
            dfs(l[:i]+l[i+1:],temp.append([l[i]]))
    res = []
    s = s.sort()  
    dfs(s,[])
    return res


class Solution:
    def permutation(self, s):
        # inputs: s: str
        # outputs: List[str]

        def dfs(index):
            if index == len(s) - 1:
                # join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串。在这里将list of str转换为str
                res.append(''.join(s))  
                return
            d = set()
            for i in range(index,len(s)):
                if s[i] in d:
                    continue
                d.add(s[i])
                s[i],s[index] = s[index],s[i]  # swap 在index-len中每哥数都有机会在i这个位置上，即固定第i位置
                dfs(index+1)
                s[i],s[index] = s[index],s[i]
        s = list(s)
        res = []
        dfs(0)
        return res

class Solution_2:
    def permutation(self, s):
        # inputs: s: str
        # outputs: List[str]
        if not s:
            return 
        def dfs(s,temp):
            if not s:
                # join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串。在这里将list of str转换为str
                res.append(''.join(temp))  
                return
            for i,char in enumerate(s):
                if i>0 and s[i] == s[i-1]:
                    continue
                dfs(s[:i]+s[i+1:],temp+[char])
        s = list(sorted(s))
        res = []
        dfs(s,[])
        return res
        