# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None
        def recur(root, p, q):
            if not root or root.val==q.val or root.val==p.val: return root 
            left = recur(root.left,p,q)
            right = recur(root.right,p,q)
            if left and right: return root
            elif left or right: return left or right
            else: return None
        return recur(root, p, q)