# 题意：一次翻转k个链表  错题❌！！！

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self, head, tail):
        prev = tail.next
        p = head
        while prev!=tail:
            nex = p.next
            p.next = prev
            prev,p = p,nex
        return tail,head

    def reverseKGroup(self, head, k):
        # 创建多余的头节点
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            # 检查是否满足k个
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail: return dummy.next
            # 开始翻转
            nxt = tail.next
            head, tail = self.reverse(head,tail)
            #pre.next = head
            pre.next,tail.next = head,nxt
            pre,head = tail,nxt
        return dummy.next
   
    