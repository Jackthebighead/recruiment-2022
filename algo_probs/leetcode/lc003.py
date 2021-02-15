# 题意：给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 解法：滑动窗口法：需要维护一个不重复字符子串的表，一个当前表长度，历史最大表长度。循环字符串，对每个字符若不重复添加；若重复则从左到右删除字符到满足不重复子串，之后再添加。
# 注意：1. 可以用set，若用set则需要再设置一个left指针来记录删除 2. 对于for循环range内的长度可以先赋值到n，这样节省时间。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # inputs: s: str
        # outputs: int
        if not s:
            return 0 
        lookup = []
        cur_len = 0
        max_len = 0
        n = len(s)
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.pop(0)
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.append(s[i])
        return max_len

class Solution_2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len

     
