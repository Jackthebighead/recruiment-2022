# 题意：请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。若队列为空，pop_front 和 max_value 需要返回 -1
# 题解：题目要求了O(1)的时间，故不能用维护一个最大值变量/指针来解决，因为在最大值pop后不知道下一个最大值在哪，只能考虑用空间看时间用辅助数据结构来解决。
# 题目要求队列中的最大值，我们可以考虑维护一个额外的递减队列，队列的[0]是最大[-1]是最小。对于一个元素push，判断这个元素和队尾-1的大小，若比队尾大让队尾元素弹出，再插入当前元素。
# 这么判断是因为维护一个递减序列的话，只有出现在队列最大值之后的且比最大值小的会被记录，正好是我们需要的，而push的时候被弹出的没必要，因为这些都出现在当前元素之前且比它小，记录的话没有意义。

class MaxQueue:

    def __init__(self):
        from collections import deque
        self.deque = deque()
        from queue import Queue
        self.queue = Queue()

    def max_value(self) -> int:
        if not self.deque: return -1
        else: return self.deque[0]

    def push_back(self, value: int) -> None:
        self.queue.put(value)
        while self.deque and value>self.deque[-1]: self.deque.pop()
        self.deque.append(value)
        
    def pop_front(self) -> int:
        if self.queue.empty(): return -1
        temp = self.queue.get()
        if temp == self.deque[0]: self.deque.popleft()
        return temp


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()