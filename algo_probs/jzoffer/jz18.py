# 题意：链表listnode删除指定val的节点
# 题解1: 双指针，用pre和cur
# 题解2: 单指针，如果head.next的val等于val，那么对head.next.next接上head
# 上述两个方法都要对head先进行判断
# 题解3: 递归，思想是递归一下head.next，满足就返回head.next,不满足接着走，走到底返回head，最后操作一遍后返回head。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head, val):
        # inputs: head: ListNode, val: int
        # outputs: ListNode
        if not head:
            return None
        if head.val == val:  # 先对头节点进行判断，才好带入while循环
            return head.next
        
        pre, cur = head, head.next
        while cur and cur.val!=val:  # 如果不把cur.val!=val加在while上那么在loop里面if的时候如果满足条件之后要break减少不必要计算
            pre, cur = cur, cur.next
        if cur:
            pre.next = cur.next
        return head



class Solution_2:
    def deleteNode(self, head, val):
        # inputs: head: ListNode, val: int
        # outputs: ListNode
        if not head:
            return None
        if head.val == val:
            return head.next
        res = head
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
                break
            head = head.next
        return res

class Solution_3:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head: 
            return head
        if head.val == val:
            return head.next
        head.next = self.deleteNode(head.next, val)
            
        return head

