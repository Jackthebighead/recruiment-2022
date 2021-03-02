# 题意：二叉树的第k大节点问题，给定一棵二叉搜索树，请找出其中第k大的节点。
# 题解1: 中序遍历把树结构变成列表求出排序数组，然后输出第k个。空间复杂度O(n)
# 题解2: 思路一样，优化了以下，用self.k和self.res保留结果，节省空间复杂度。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root, k):
        # inputs: root: TreeNode, k: int
        # outputs: int
        # 中序遍历将搜索树转化为排序列表然后输出大数字
        if not root:
            return 
        res = []
        def recur(root):
            if root.right: recur(root.right)
            res.append(root.val)
            if root.left: recur(root.left)
        recur(root)
        return res[k-1]

class Solution_2:
    def kthLargest(self, root, k):
        # inputs: root: TreeNode, k: int
        # outputs: int
        def recur(root):
            if not root: return
            recur(root.right)
            if self.k == 0:
                return 
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            recur(root.left)
        self.k = k
        recur(root)
        return self.res