# 题意：二叉树中和为某一值的路径。输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
# 题解：前序遍历+回溯
# 比较经典的解法，维护一个路径记录的global变量path，前序遍历树，若到底且满足条件则加入到结果中，不满足则，回溯，这里回溯用pop即可实现。
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        # inputs: root: TreeNode, sum: int
        # outputs: List[List[int]]
        
        # 用递归
        res,path = [],[]
        def recur(root,cnt):
            if not root:
                return 
            path.append(root.val)
            cnt -= root.val
            if cnt == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, cnt)
            recur(root.right, cnt)
            path.pop()  # 回溯
        recur(root,sum)
        return res
        
