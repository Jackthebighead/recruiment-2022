# 题意：输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
# 题解1: 将链表的node依次放入一个栈，然后对k循环进行pop。当然，也可以将node放入一个list然后print第-k个点。
# 题解2: 双指针法，记录n和n-k指针。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head, k):
        if not head:
            return 
        stack = []
        # temp = head
        while head:
            stack.append(head)
            head = head.next
        return stack[-k]


class Solution_2:
    def getKthFromEnd(self, head, k):
        if not head:
            return 
        res = head  # # 令res为head，解决了当只有一个节点返回倒数第一个时候的情形
        for _ in range(k):
            head = head.next
        while head:
            res = res.next
            head = head.next
        return res

class Solution_3:
    def getKthFromEnd(self, head, k):
        if not head:
            return 
        res,cnt = head,0  # 令res为head，解决了当只有一个节点返回倒数第一个时候的情形
        while head:
            if cnt >=k:
                res = res.next
            head = head.next
            cnt += 1
        return res




        



