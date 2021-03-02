# 题意：
# 题解1:用库函数strip+split+remove+join，其中，list变str用''.join()，list中删除某元素list.remove，删除所有用while，字符串两侧取消空格用str.strip，字符串变成list用str.split
# 题解2: 用快慢指针，注意边界即可

class Solution:
    def reverseWords(self, s):
        # inputs: s: str
        # outputs: str
        res = s.strip(' ').split(' ')
        while '' in res: res.remove('')
        return ' '.join(res[::-1])

class Solution_2:
    def reverseWords(self, s):
        # inputs: s: str
        # outputs: str
        # 快慢指针
        data = s.strip(' ')
        res,i,j = [],0,0
        while i<=len(data)-1:
            while i<=len(data)-1 and data[i]!=' ': i+=1
            res.append(data[j:i] if i<len(data)-1 else data[j:i+1])
            while i<=len(data)-1 and data[i]==' ': i+=1
            j = i
        return ' '.join(res[::-1])