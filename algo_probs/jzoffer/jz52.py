# 题意：输入两个链表，找出它们的第一个公共节点。
# 题解1: 双指针解决不等长链表找共哦那个节点问题，可以将两个表对齐，先让长的链表的指针走，等走到同长的时候一起走直到遇到node地址相同时返回。
# 这题需要注意的是，这里的公共节点是值节点的地址相同而不是节点的val相同，故比较的时候需要比较
# 题解2: tricky，看成一个相互追逐的游戏，双指针同时走，若一个走完从下一个链表的头节点开始，直到两者相遇。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        # inputs: headA: ListNode, headB: ListNode
        # outputs: ListNode
        # 对齐两个链表，先走长的链表，走到和短链表一样长时双指针一起遍历，直到发现公共节点
        if not headA or not headB:
            return None
        len_a,len_b,a,b,res = 0,0,headA,headB,None
        while a:
            len_a += 1
            a = a.next
        while b:
            len_b += 1
            b = b.next
        for i in range(abs(len_a-len_b)):
            if len_a>len_b:
                headA = headA.next
            else:
                headB = headB.next
        while headA:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next
        return None


class Solution_2:
    def getIntersectionNode(self, headA, headB):
        # inputs: headA: ListNode, headB: ListNode
        # outputs: ListNode
        # 对齐两个链表，先走长的链表，走到和短链表一样长时双指针一起遍历，直到发现公共节点
        if not headA or not headB:
            return None
        a,b = headA,headB
        while a!=b:
            a,b = a.next if a else headB, b.next if b else headA
        return a


            

            
            

            