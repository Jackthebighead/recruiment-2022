# 题意：判断树的子结构：输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)。B是A的子结构， 即 A中有出现和B相同的结构和节点值。
# 题解：递归。
# 本题属于匹配类二叉树题目，一般做法就是递归。可以分为两个步骤，首先是找到匹配的跟节点，其次是对于根节点接着匹配下去看是否能匹配成功
# 在本题，找到根节点需要递归调用自身，找到根节点后用自定义的递归函数递归地匹配。整个过程用or and 等bool算子来拼凑成最后结果。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A, B) -> bool:
        # inputs: A: TreeNode, B: TreeNode
        # outpus: bool
        if not B or not A:
            return False
        def recur(A, B):
            if not A and not B:
                return True
            elif not A:
                return False
            elif not B:
                return True
            else:
                # 值不相等
                if A.val != B.val:
                    return False
                # 值相等
                else:
                    return recur(A.left, B.left) and recur(A.right, B.right)
        return recur(A, B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right, B)

# 简介写法        
class Solution_2:
    def isSubStructure(self, A, B):
        if not A or not B:
            return False
        def recur(A, B):
            # 如果无B
            if not B:
                return True
            # 如果有B
            if not A:
                return False
            # 如果有B有A
            return (recur(A.left, B.left) and recur(A.right, B.right)) if A.val == B.val else False
        return recur(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right, B)