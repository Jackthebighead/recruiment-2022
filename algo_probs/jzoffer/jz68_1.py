# 题意：二叉搜索树的最近公共祖先
# 题解1：递归，注意每个元素都是特异的。从上往下递归，用left和right表示当前节点的左子树是否含有pq，若否则为None，若是则返回该节点，以此递归。递归方程运行完从下往上最每个节点判断：当左右子树都有节点说明当前root是公共祖先，若左右只有一个那么有的那个是公共祖先，一直向上传递即可。
# 因为每个元素是特异的，所以这题可以不用到搜索树的性质。。当然若用则会更简单。
# 题解2: 递归，用二叉搜索树的特性，若root的值处于pq值中间则root就是祖先，若root大于qp则递归左子树，反之递归右子树
# 题解3: 迭代，用while
# 可以很明心啊的看到用迭代更慢，但空间更少

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # inputs: root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
        # outputs: 'TreeNode'
        if not root: return None
        def recur(root, p, q):
            if root==q or root==p: return root 
            if not root: return None
            left = recur(root.left,p,q)
            right = recur(root.right,p,q)
            if left and right: return root
            elif left or right: return left or right
            else: return None
        return recur(root, p, q)

class Solution_2:
    def lowestCommonAncestor(self, root, p, q):
        # inputs: root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
        # outputs: 'TreeNode'
        if p.val < root.val and q.val <root.val: return self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val  and q.val > root.val: return self.lowestCommonAncestor(root.right,p,q)
        return root

class Solution_3:
    def lowestCommonAncestor(self, root, p, q):
        # inputs: root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
        # outputs: 'TreeNode'
        while root:
            if root.val>q.val and root.val>p.val: root = root.left
            elif root.val<q.val and root.val<p.val: root = root.right
            else: break
        return root