# 题意：实现二叉树的前中后序遍历，输出到一个数组中

class Solution:
    def threeOrders(self , root ):
        # write code here
        res = [[],[],[]]
        def recur(root):
            if not root: return
            res[0].append(root.val)
            recur(root.left)
            res[1].append(root.val)
            recur(root.right)
            res[2].append(root.val)
        recur(root)
        return res