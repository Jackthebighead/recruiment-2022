# 题目：给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 进阶：你能尝试使用一趟扫描实现吗？

# 解法1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 快慢指针
        dummy = ListNode(1)
        dummy.next = head
        l,r = dummy,head
        for _ in range(n):
            r = r.next
        while r:
            l,r = l.next,r.next
        l.next = l.next.next
        return dummy.next

# 解法2: 先计算长度，再删除
# 解法3: 入栈