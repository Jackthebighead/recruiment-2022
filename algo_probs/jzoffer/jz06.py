# 题意：反转数组
# 解法1：递归，终止条件为head为None返回[]，其余返回‘递归+head.val’
# 解法2：辅助栈，Python在遍历一个链表的时候，将值依次放入到一个list中，遍历结束后，翻转list输出即可。
# 注意这里的head就是listNode结构，head其实就相当于一个头节点，调用字节点需要通过.next函数。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head):
        # head: ListNode
        # List[int]
        if not head:
            return []
        return self.reversePrint(head.next) + [head.val]


class Solution_2:
    def reversePrint(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

