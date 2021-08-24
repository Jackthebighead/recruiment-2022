# 找二叉搜索树的第k大节点

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 中序遍历，从大到小，不断地append，直到第k个
        self.res = []
        self.k=k

        def recur(root):
            if not root: return 
            # right
            if root.right: recur(root.right)
            
            # middle
            if len(self.res)==self.k: return  # 剪枝
            self.res.append(root.val)
            if len(self.res)==self.k: self.num=root.val
            
            # left
            if root.left: recur(root.left)
            
        recur(root)
        return self.num