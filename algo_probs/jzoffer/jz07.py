# 题意：根据前向遍历和中序遍历还原BFS形式的二叉树
# 解法：前序遍历的第一个是中序遍历中间的，根据此可以分成左子树和右子树。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder): 
    # input: preorder: List[int], inorder: List[int])
    # output: TreeNode
        if not preorder:
            return 
        head = TreeNode(preorder[0])
        head_index = inorder.index(head.val)
        if head_index != 0:
            head.left = self.buildTree(preorder[1:head_index+1], inorder[:head_index])
        if head_index != len(inorder) - 1:
            head.right = self.buildTree(preorder[head_index+1:], inorder[head_index+1:]) 
        return head
