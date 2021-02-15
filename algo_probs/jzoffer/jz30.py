# 题意：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
# 题解：设置辅助栈，来存当前（全局）最小的元素依次入栈。

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # 辅助栈存储当前最小的元素，所以不用担心主栈弹出后辅助栈顶是否仍是全局最小。
        self.stack_sup = []

    def push(self, x: int) -> None:
        if not self.stack_sup or x<=self.stack_sup[-1]:  # not要写在前面！
            self.stack_sup.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.stack_sup[-1]:
            self.stack_sup.pop() #= self.stack_sup[:-1]
        self.stack.pop()       

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.stack_sup[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()