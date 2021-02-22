# 题意：二叉搜索树和双向链表
# 题解1: 题意即找出所有节点的前继和后继。但Node数据结构没有。所以可以将中序遍历写出来，再链接。

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root):
        # inputs: root: 'Node'
        # outputs: 'Node'
        if not root:
            return 
        res = []
        def recur(root):
            if not root:
                return 
            recur(root.left)
            res.append(root)
            recur(root.right)
        recur(root)
        n = len(res)
        for i in range(n):
            if i>0:
                res[i].left = res[i-1]
            if i<n-1:
                res[i].right = res[i+1]
        res[0].left,res[-1].right = res[-1],res[0]
        return res[0]
