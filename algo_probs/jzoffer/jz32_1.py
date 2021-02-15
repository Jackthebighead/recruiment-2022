# 题意：从上到下打印二叉树1
# 题解1：BFS，用while
# Python 中使用 collections 中的双端队列 deque() ，其 popleft() 方法可达到 O(1)O(1) 时间复杂度；列表 list 的 pop(0) 方法时间复杂度为 O(N)O(N) 。
# 所以这道题的trick就是用双端队列

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def levelOrder(self, root):
        # inputs: root: TreeNode
        # outputs: List[int]
        import collections
        if not root:
            return []
        res,queue = [], collections.deque()
        queue.append(root)
        while queue:
            temp = queue.popleft()
            res.append(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return res
