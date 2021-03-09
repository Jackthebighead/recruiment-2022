# 题意：找到字符串中最长无重复的子串 （错题❌！！！！）
# 哈希+快慢指针

class Solution:
    def maxLength(self , arr ):
        # write code here
        # 快慢指针+哈希法
        j = 0
        dic = {}
        res = 0
        for i in range(len(arr)):
            if arr[i] in dic:
                j = max(j,dic.get(arr[i]))
            dic[arr[i]] = i
            res = max(res,i-j)
        return res