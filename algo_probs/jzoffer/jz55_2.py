# 题意：判断是否是平衡二叉树
# 这题的核心是：树的深度等于左子树的深度与右子树的深度中的最大值+1。即 depth=max(recur(left),recur(right))+1 如果左右相差小于1，不然为-1（False）
# 题解1: 暴力解法，递归从上往下判断root的左右子树深度是否相差大于1
# 题解2: 真正的递归解法：递归到最下层，自下而上统计左右长度，若长度相差大于1返回不为平衡树（-1）
# trick在于用-1代表不为平衡树，若为-1直接退出，剪枝，减少时间复杂度。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        # inputs: root: TreeNode
        # outputs: bool
        # 左子树的深度与右子树的深度相差不超过1
        if not root: return True
        def get_depth(root):
            if not root: return 0
            return 1 + max(get_depth(root.left),get_depth(root.right))
        if abs(get_depth(root.left)-get_depth(root.right))<=1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else: return False 

class Solution_2:
    def isBalanced(self, root):
        # inputs: root: TreeNode
        # outputs: bool
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left==-1: return -1  
            right = recur(root.right)
            if right==-1: return -1
            return max(left,right)+1 if abs(left-right)<=1 else -1  # max+1为深度
            # -1: 剪枝，若出现不是平衡树的子树立刻返回，设计-1是为了可以融合和子树深度和是否为平衡树两个条件
        return recur(root)!=-1
            