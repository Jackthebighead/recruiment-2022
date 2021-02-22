# 题意：从上到下打印二叉树2
# 题解1：仍旧是BFS，只不过多了些队列的处理，增加来辅助列表
# 题解2: 递归，引入depth(深度)的做法，fork了别人的，作为了解。大意就是用depth来控制插入的位置

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        import collections
        if not root:
            return []
        res,queue = [], collections.deque()
        queue.append(root)
        while queue:
            # 设置res_temp存中间结果，即每一层的节点的val
            res_temp = []
            for _ in range(len(queue)):
                temp = queue.popleft()
                res_temp.append(temp.val)
                # 双端队列左边出右边进
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            res.append(res_temp)
        return res


class Solution_2:
    def levelOrder(self, root):
        if not root: return []
        res = []
        def helper(root, depth):
             # 初始len为0，depth为0，在res加第一层即res[0]=[]，然后不断更新，做到每depth+1迭代就对应len(res)+1
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)  # 用res[depth]来控制插入的位置
            if root.left: helper(root.left, depth + 1)
            if root.right: helper(root.right, depth + 1)
        helper(root, 0)
        return res