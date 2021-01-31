# 题意：用两个栈实现一个队列
# 解法：用python的两个列表模拟双栈，一个进一个出。

class CQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def appendTail(self, value):
        self.stack_in.append(value)

    def deleteHead(self):
        if not self.stack_out:
            if not self.stack_in:
                return -1
            else:
                while self.stack_in:
                    self.stack_out.append(self.stack_in.pop())
                return self.stack_out.pop()
        else: return self.stack_out.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()