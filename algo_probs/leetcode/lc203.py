# 题目：给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
 
# 解法1
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # iteration
        dummy = ListNode(2)
        dummy.next = head
        pre,p = dummy,head
        while p:
            if p.val==val:
                pre.next = p.next
                p = p.next
            else: pre,p = p,p.next
        return dummy.next
        
#解法2
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # iteration
        if not head: return 
        head.next = self.removeElements(head.next,val)
        return head if head.val!=val else head.next