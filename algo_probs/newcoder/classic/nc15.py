# 题意：输出层序遍历
# 题解：递归，迭代

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# 
# @param root TreeNode类 
# @return int整型二维数组
#
class Solution:
    def levelOrder(self , root ):
        # write code here\
        if not root: return []
        res = []
        from collections import deque
        q1 = deque()
        q1.append(root)
        while q1:
            temp = []
            for _ in range(len(q1)):
                node = q1.popleft()
                temp.append(node.val)
                if node.left: q1.append(node.left)
                if node.right: q1.append(node.right)
            res.append(temp)
        return res

class Solution_2:
    def levelOrder(self , root ):
        # write code here\
        if not root: return []
        res = []
        def recur(root,level):
            if len(res)==level: res.append([])
            res[level].append(root.val)
            if root.left: recur(root.left, level+1)
            if root.right: recur(root.right, level+1)
        recur(root,0)
        return res