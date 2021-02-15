# 题意：给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。请你将两个数相加，并以相同形式返回一个表示和的链表。你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 解法1: 用while来迭代。考虑两点：进位和不同长两个情况，分别采用：设置一个进位变量，和当某个输入为None(短的已遍历完)时输入的val为0. 对于链表移动，需要先初始化节点，再赋值给一个空指针，在循环内部用next迭代节点。
# 解法2: dfs思路递归。除了判断边界情况，与迭代的while循环不同的是，这里不用初始化，每次递归先给当前节点赋值，再令节点的next和下一个递归结果相等，即可完成一个链表。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 解法1:
class Solution:
    def addTwoNumbers(self, l1, l2):
        # input: l1: ListNode, l2: ListNode
        # output: ListNode
        jw = 0
        node = ListNode(0)  # 初始化
        p = node  # 因为node要进行迭代，所以把node的初始值赋给另一个指针
        while l1 or l2 or jw:
            temp = (l1.val if l1 else 0) + (l2.val if l2 else 0) + jw
            res = temp%10
            jw = temp//10

            # ListNode结构用这种方法遍历+构造链表
            node.next = ListNode(res) 
            node = node.next
            l1,l2 = l1.next if l1 else None, l2.next if l2 else None
        return p.next

# 解法2:
class Solution_2:
    def dfs(self, l1, l2, jw):
        if not l1 and not l2 and jw==0:
            return None
        res = (l1.val if l1 else 0) + (l2.val if l2 else 0) + jw
        jw = res//10
        p = ListNode(res%10)
        l1,l2 = l1.next if l1 else None,l2.next if l2 else None
        p.next = self.dfs(l1,l2,jw)
        return p

    def addTwoNumbers(self, l1, l2):
        # input: l1: ListNode, l2: ListNode
        # output: ListNode
        if not l1 and not l2:
            return None
        elif not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1
        else:
            return self.dfs(l1,l2,0)