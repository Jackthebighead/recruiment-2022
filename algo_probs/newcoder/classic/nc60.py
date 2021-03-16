# 题意：判断一棵树是否是完全+搜索二叉树
# 题解：分别判断，不用递归。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
# 
# @param root TreeNode类 the root
# @return bool布尔型一维数组
#
class Solution:
    def judgeIt(self , root ):
        # write code here
        # 完全二叉树：左右子节点不为空，搜索二叉树：左小右大
        if not root: return [True,True]
        return [self.is_bst(root),self.is_fbt(root)]
        
    def is_bst(self, root):
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
    
    def is_fbt(self,root):
        # 用指标i记录节点序数的方法
        res = [(root,1)]
        i = 0
        while i<len(res):
            node,l = res[i]
            if not node: continue  # redundant
            else:
                if node.left: res.append((node.left,l*2))
                if node.right: res.append((node.right,l*2+1))
            i+=1 
        return res[-1][1] == len(res)