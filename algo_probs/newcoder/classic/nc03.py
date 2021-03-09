# 题意：找到环的入口节点

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def detectCycle(self , head ):
        # write code here
        # fast and slow
        slow=head
        fast=head
        while True:
            if not fast or not fast.next: return
            slow=slow.next
            fast=fast.next.next
            if fast==slow: break
        fast=head
        while fast!=slow:
            fast=fast.next
            slow=slow.next
        return fast