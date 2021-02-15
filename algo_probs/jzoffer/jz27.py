# 题意：二叉树的镜像问题。请完成一个函数，输入一个二叉树，该函数输出它的镜像。
# 题解1: 递归，solution1稍微麻烦。。solution2是精简版，从上到下递归自己。
# 题解2: 用辅助栈来BFS，对每层实现交换。对每次弹出的，交换left和right，如果有left加入栈，以此类推。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root):
        # inputs: root: TreeNode
        # outputs: TreeNode
        if not root:
            return
        def recur(root):
            if not root:
                return
            else:
                root.left, root.right = root.right, root.left
                recur(root.right)
                recur(root.left)
                return root

        return recur(root)

class Solution_2:
    def mirrorTree(self, root):
        # inputs: root: TreeNode
        # outputs: TreeNode
        if not root:
            return
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        # 如果不平行赋值，就要用tmp先存储left或者right，否则递归赋值的时候该节点已经被改变了
        return root

class Solution_3:
    def mirrorTree(self, root):
        # inputs: root: TreeNode
        # outputs: TreeNode
        if not root:
            return 
        stack = [root]
        while stack:
            deal = stack.pop()
            if deal.left: stack.append(deal.left)
            if deal.right: stack.append(deal.right)
            deal.left, deal.right = deal.right, deal.left
        return root