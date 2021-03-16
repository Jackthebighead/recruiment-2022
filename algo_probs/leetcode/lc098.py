# 题意：判断是否为二叉搜索树
#假设一个二叉搜索树具有如下特征：节点的左子树只包含小于当前节点的数。节点的右子树只包含大于当前节点的数。所有左子树和右子树自身必须也是二叉搜索树。
# 题解1: 递归
# 题解2: 变为中序遍历
# 题解3: 迭代

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        if not root: return True
        def recur(root, lower, upper):
            if not root: return True
            # 若满足当前节点在该层的搜索树性质，递归下面
            if lower<root.val<upper:
                left = recur(root.left,lower, root.val)
                right = recur(root.right,root.val, upper)
                if left and right: return True
                else: return False
            else: return False
        return recur(root, float('-inf'), float('inf'))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_2:
    def isValidBST(self, root):
        inorder = []
        if not root: return True
        def recur(root):
            if not root: return 
            recur(root.left)
            inorder.append(root.val)
            recur(root.right)
        recur(root)
        return True if all(inorder[i]>inorder[i-1] for i in range(1,len(inorder))) else False