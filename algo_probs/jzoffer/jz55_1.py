# 题意：求二叉树的深度
# 题解：递归

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        # inputs: root: TreeNode
        # outputs: int
        def recur(root, cnt):
            if not root: return cnt
            return max(recur(root.left, cnt+1),recur(root.right, cnt+1))
        return recur(root,0)