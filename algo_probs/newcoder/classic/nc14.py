# 题意：层序遍历二叉树，遇到奇数层反向
# 这里蠢办法是对奇数层和偶数层，用插入下一层子节点到双端队列q的方向不同来实现反向。
# 好办法是用cnt记录奇数和偶数，在每次插入res的temp数组中用双端队列的不同插入方向来实现反向

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
    def zigzagLevelOrder(self , root ):
        # write code here
        # 广度遍历，用while+queue
        if not root: return []
        from collections import deque
        q = deque()
        q.append(root)
        res = []
        while q:
            temp = deque()
            for _ in range(len(q)):
                if len(res)%2==0:
                    node = q.popleft()
                    temp.append(node.val) 
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                else:
                    node = q.pop()
                    temp.append(node.val) 
                    if node.right: q.appendleft(node.right)
                    if node.left: q.appendleft(node.left)
            res.append(temp)
        return res