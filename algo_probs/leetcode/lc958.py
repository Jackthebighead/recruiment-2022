# 题意：检验树是完全二叉树给定一个二叉树，确定它是否是一个完全二叉树。百度百科中对完全二叉树的定义如下：若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。（注：第 h 层可能包含 1~ 2h 个节点。）
# 题解1: 用性质判断。若一棵树是完全二叉树。若当前节点只有右子树，那么不为完全二叉树；若当前节点有两个孩子或只有左孩子，那么该节点之后的 后续节点都不能有孩子。
# 而上述“后续节点”可以通过BFS来得到
# 题解2: 用一个tuple记录，(root,i)，其中根节点的i为1，对任何一个节点，左孩子的i为i*2，右孩子的i为i*2+1。BFS遍历。若最后BFS输出的数组的最后一个元素的第二个元素不为整个数组的长度，则不为完全二叉树。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root):
        import collections
        # 广度优先的方法
        if not root: return True
        q = collections.deque()
        q.append(root)
        flag = False
        while q:
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

            if not node.left and node.right: return False
            # 若此前已经有“无左无右的节点，或只有左的节点 ”，那么BFS遍历的后面必须也都是这样的节点    
            if flag and (node.left or node.left): return False
            if (not node.left and not node.right) or (not node.right and node.left):
                flag = 1
        return True

class Solution_2:
    def isCompleteTree(self, root: TreeNode) -> bool:
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