# 题意：二叉树公共祖先

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# 
# @param root TreeNode类 
# @param o1 int整型 
# @param o2 int整型 
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self , root , o1 , o2 ):
        # write code here
        def recur(root,o1,o2):
            if not root or root.val==o1 or root.val==o2: return root
            left = recur(root.left,o1,o2)
            right = recur(root.right,o1,o2)
            if right and left: return root
            elif not right and not left: return None
            elif not left: return right
            else: return left
        return recur(root,o1,o2).val