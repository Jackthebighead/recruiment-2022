# 题意：k个一组反转链表
# 主要考察对思路转化为代码的问题，边界情况要注意
# 主题思路是两个
# 1. 首先定义主函数，我们在实现反转的时候，首先要从头开始往后遍历k个如果都满足不为空则说明该次可以进行k个数字反转，若有空则直接返回即可。
# 2. 其次进行置换，注意将反转部分和该部分前面的节点，后面的节点相连。
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/k-ge-yi-zu-fan-zhuan-lian-biao-by-leetcode-solutio/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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
            pre.next = head
            #pre.next,tail.next = head,nxt
            pre,head = tail,nxt
        return dummy.next