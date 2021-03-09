# 题意：判断是否是环形链表
# 题解1: 遍历每个节点，若下一个节点的next不指向自己，则继续且将该节点的next指向自己，移动；反之则返回True。该方法将遍历过的节点都指向自己，若之后有节点指向前面的节点形成环，那么该节点的next的next必指向自己
# 题解2: 快慢指针，快指针一次走两步，慢一次走一步，若能追上则是环


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        if not head: return False
        p = head
        while p:
            if not p.next: return False
            if p.next==p: return True
            head.next = head
            p,head = p.next,p
        return False

class Solution_2:
    def hasCycle(self, head):
        if not head or not head.next: return False
        slow,fast = head,head.next
        while fast!=slow:
            if not fast.next or not fast.next.next: return False
            else: fast = fast.next.next
            slow = slow.next
        return True