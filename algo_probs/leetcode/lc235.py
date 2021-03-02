# 题意：找二叉搜索树中两节点的公共祖先
# 题解：利用搜索树的性质，分析root.val跟q.val和p.val的大小关系来讨论
# 合并if语句，发现p为q的root的情况是可以一起写到else中的，见solution_2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # inputs: p: 'TreeNode', q: 'TreeNode'
        # outputs: 'TreeNode' 
        if not root or root == p or root == q: return root
        if min(p.val,q.val)<root.val<max(q.val,p.val): return root
        elif root.val>max(p.val,q.val): return self.lowestCommonAncestor(root.left,p,q)
        else: return self.lowestCommonAncestor(root.right,p,q)


class Solution_2:
    def lowestCommonAncestor(self, root, p, q):
        # inputs: p: 'TreeNode', q: 'TreeNode'
        # outputs: 'TreeNode' 
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root