# 题意：对称二叉树问题。请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
# 题解1:非递归做法，用两个辅助栈，配合dfs。一个栈记录左子树，一个记录右子树。入栈顺序不同来实现每次弹出比较镜像对象。
# 题解1改良：用collection.deque的双端队列来完成。
# 题解2: 递归做法。判断左子树右子树。要分两个phase来讨论：若都不存在则true，若只有一个存在则false，若都存在则进入下一个phase
# 若存在且两者val相同则递归 左的左，右的右 and 递归 左的右，右的左。若不相同则false。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        # inputs: root: TreeNode
        # outputs: bool
        # 非递归方法
        if not root:
            return True
        stack_left, stack_right = [],[]
        stack_left.append(root.left)
        stack_right.append(root.right)
        while stack_right or stack_left:
            left = stack_left.pop()
            right = stack_right.pop()
            if not left and not right:  # 这里是continue，因为此时也存在是对称树的可能性
                continue
            elif not left or not right:
                return False
            else:
                if left.val != right.val:
                    return False
                stack_left.append(left.right)
                stack_left.append(left.left)
                stack_right.append(right.left)
                stack_right.append(right.right)
        return True


class Solution_2:
    def isSymmetric(self, root):
        # inputs: root: TreeNode
        # outputs: bool
        # 非递归方法
        if not root:
            return True
        
        # 用双端队列
        from collections import deque
        queue = deque()
        queue.appendleft(root.left)
        queue.append(root.right)
        while queue:
            left = queue.popleft()
            right = queue.pop()
            if not left and not right:  # 这里是continue，因为此时也存在是对称树的可能性
                continue
            elif not left or not right:
                return False
            else:
                if left.val != right.val:
                    return False
                queue.appendleft(left.right)
                queue.appendleft(left.left)
                queue.append(right.left)
                queue.append(right.right)
        return True

class Solution_3:
    def isSymmetric(self, root):
        # inputs: root: TreeNode
        # outputs: bool
        # 递归方法
        if not root:
            return True
        def recur(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                if left.val != right.val:
                    return False
                return recur(left.left, right.right) and recur(left.right, right.left) 
        return recur(root.left, root.right)

        