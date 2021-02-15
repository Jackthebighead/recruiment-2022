# 题意：合并两个排序的链表。输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
# 题解1: 本题需要注意三个地方：边界（两个链表是否为空），改变链序，处理不等长链表情况
# 改变链序的过程：首先让l1是头节点val最小的那个（或者也可以新建一个头节点。。这样并不会增加什么空间复杂度），再让l1为l1.next，用while循环依次比较l1和l2的val，谁小reference链谁，链完l=l.next，
# 下一个循环开始前reference也要自增。这里要用两个reference一个用来比较修改，一个用来最后返回整体
# 题解2: 用递归写，大同小异，也是比较头节点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        # inputs:l1: ListNode, l2: ListNode:
        # outputs: ListNode
        # 首先考虑边界情况
        if not l1 and not l2:
            return 
        elif not l1:
            return l2
        elif not l2:
            return l1
        else:
            if l2.val<l1.val:
                l1,l2 = l2,l1  # 让l1是更小的那个
            res = l1
            res_f = res
            l1 = l1.next
            while l1 and l2:
                if l1.val > l2.val:
                    res.next,l2 = l2,l2.next
                else:
                    res.next,l1 = l1,l1.next
                res = res.next
            # 处理不等长情况
            res.next = l1 if not l2 else l2
            return res_f



                    
                
                
                
            