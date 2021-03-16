# 题意：删除链表的倒数第n个节点

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 
# @param n int整型 
# @return ListNode类
#
class Solution:
    def removeNthFromEnd(self , head , n ):
        # write code here
        # 三指针
        pre,cur,fast = None,head,head
        for _ in range(n): fast = fast.next
        while fast:
            pre,cur,fast = cur,cur.next,fast.next
        pre.next = cur.next
        return head