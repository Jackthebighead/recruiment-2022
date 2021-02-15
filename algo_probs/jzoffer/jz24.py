# 题意：反转列表。定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
# 题解1: 三指针，当nxt为空的时候返回cur，在每次while内将cur的next指到pre，然后用nxt来推动循环。或者是双指针但在迭代中nxt用temp=cur.next来存起来
# 题解2: 双指针，pre和cur，用递归的做法。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        # inputs: listnode
        # outputs: listnode
        if not head:
            return 
        pre, cur, nxt = None, head, head.next
        if not nxt:
            return cur
        while cur:
            cur.next = pre
            if not nxt:
                break
            else:
                pre,cur,nxt = cur,nxt,nxt.next
        return cur

class Solution_2:
    def reverseList(self, head):
        # inputs: listnode
        # outputs: listnode
        if not head:
            return 
        def recur(pre,cur):
            if not cur: 
                return pre
            res = recur(cur,cur.next)
            cur.next = pre
            return res  # 返回链表头节点
     
        return recur(None, head)