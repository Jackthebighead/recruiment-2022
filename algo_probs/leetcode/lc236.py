# 题意：找二叉树中两节点的公共祖先
# 与上一题相同，但条件从二叉搜索树变成了二叉树
# 题解：也是递归
# 对于一个二叉树，若两个点有一个公共节点root，那么root有以下几种可能
# 1. 两个点在root左右两侧，那么输出root即可
# 2. 两个点在root同侧，接着递归子树：
# 2.1 p在q的子树下：返回q即可
# 2.2 q在p的子树下：返回p即可
# 所以递归应该设计为：从上倒下，若root等于q或者p返回root即可；对于root有left和right，left为递归root.left，right为递归root.right。
# 若left为空或right为空，说明在同侧，返回不为空的变量即可，该变量既是q和p中在上面的那个
# 若left和right同时不为空，说明在异侧，返回当前递归到的root即可。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # boundary
        if not root or root == p or root == q:
            return root
        # recurrence
        left = self.lowestCommonAncestor(root.left, p, q)  # left最后返回的是p或q，如果p或q存在与子树
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left or not right:  # 若在同侧，返回从上到下先遍历到弹出的那个
            return left or right
        else:  # 若在异侧，返回自己
            return root