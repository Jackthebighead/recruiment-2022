# 题意：复制一个复杂链表，这个链表不只有next指针还有random指针。请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
# 本题的难点在于复制，由于python中的浅拷贝和深拷贝，我们不能只是将头节点浅拷贝或者将复制品的next或者random指针指向原链表的节点。
# 解法1: 思路是先复制，再链接。复制即把所有节点都Node(val)复制一遍，然后再一一对应链接。这里如果不考虑新建一个链或者在原链表上修改的话。我们考虑哈希法。
# 在python中哈希就是建立一个键值对的字典dict={}，key是原链表节点，value是复制节点。然后在链接过程用dict[]和dict.get()就能获取节点。

# 解法2: 思路也是先复制，再链接。这时我们可以考虑在原链表上修改，先合并，后拆分
# 合并是指先通过一个循环把每个节点复制再串联到原链表中。1，1，2，2，3，3这样，通过next来链接。然后再遍历一遍复制random指针，修改(新建)复制节点的random指针指向。拆分过程就是将所有复制品拆开来就好。

# 解法3: hacky way，用copy.deepcopy()即可。。


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        # inputs: head: 'Node'
        # outptus: 'Node'
        # 由于该复杂链表多了一个random指针，若通过cur=cur.next来移动的话random不能正确赋值，只能赋值引用，浅拷贝。
        # 先将所有节点都初始化复制一遍，再考虑next和random指向问题
        d = {}
        cur = head
        while cur:
            d[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            # dict.get()获取键的值，这里得用d.get因为我们需要链接的是复制的而不是原来的cur
            d[cur].next, d[cur].random = d.get(cur.next),d.get(cur.random)  
            cur = cur.next
        return d.get(head)


class Solution_2:
    def copyRandomList(self, head):
        # inputs: head: 'Node'
        # outptus: 'Node'
        # 合并，串联的方法
        # 将每个节点复制并串联，1，1，2，2，3，3...
        if not head:
            return 
        cur = head
        while cur:
            node = Node(cur.val)
            node.next = cur.next
            cur.next = node
            cur = node.next
        # 复制节点的random
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 拆分链表
        cur = res = head.next
        while cur.next:
            cur.next = cur.next.next
            cur = cur.next
        return res


class Solution_3:
    def copyRandomList(self, head):
        import copy 
        return copy.deepcopy(head)

        
        

        
        