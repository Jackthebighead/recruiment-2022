# 题意：栈的压入和弹出的序列
# 
# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。
# 题解: 模拟法，根据栈的特性模拟出入顺序，若匹配则返回True。
# 栈，入栈的操作是先入，再比较poped，若相同则输出，stack和popoed都弹出栈顶，再接着比较下一个是否相同，若相同一直弹出，不同就push下一个，etc. 最后若stack空就全部匹配。
# 麻烦方法：考虑所有可能。题目指出 pushed 是 popped 的排列 。因此，无需考虑 pushed 和 popped 长度不同 或 包含元素不同 的情况。
# 简单方法，用辅助栈stack，先入栈，再将栈顶与poped匹配，若匹配则接着匹配下去，若不匹配则下一个pushed元素入栈

class Solution:
    def validateStackSequences(self, pushed, popped):
        # inputs: pushed: List[int], popped: List[int]
        # outputs: bool
        if not pushed and not popped:
            return True
        elif not pushed or not popped:
            return False
        stack,res,n = [],0,len(popped)
        while pushed:
            # pushed是比较当前是否符合，符合的，若stack也没有，那么移动res即可，若stack有则比较，不符合的暂存到stack中
            # 可以改进为直接都放到stack中若符合就一直（用while）匹配（因为没有重复数字，若有则更复杂），若不符合就下一个
            if pushed[0] != popped[res]:
                if stack and stack[-1] == popped[res]:
                    stack.pop()
                    res += 1 
                else:
                    stack.append(pushed[0])
                    pushed.pop(0)
            else:
                pushed.pop(0)
                res += 1
        # 这一段是判断长度不同或包含元素不同的情况的代码，但此题无需考虑
        #while stack and res<=n:
        #    if stack.pop() != popped[res]:
        #        break
        #    res += 1

        return stack[::-1] == popped[res:]


class Solution_2:
    def validateStackSequences(self, pushed, popped):
        # inputs: pushed: List[int], popped: List[int]
        # outputs: bool
        stack,res,n = [],0,len(popped)
        for item in pushed:
            # 先入栈
            stack.append(item)
            # 若相同 一直 比较下去， 一直
            while stack and stack[-1]==popped[res]:
                stack.pop()
                res += 1
        return not stack
