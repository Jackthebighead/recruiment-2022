# 题意：序列化和反序列化二叉树。实现两个函数。
# 该题的意思就是在考虑null节点的情况下（返回的list的长度是一个完全二叉树的节点个数）层序遍历二叉树，返回str，再根据str复现原二叉树
# 题解1: 层序遍历 BFS。用双端队列实现，主要就是null节点的处理。
# BFS有两种写法
# 第一种，从队列pop出来的，若有左孩子则入队列，若有右孩子则入队列，见jz32_1从上到下打印二叉树
# 第二种，从队列出来的，若为None则不操作，若部位none则左右孩子入队列
# 该题明显是第二种可取


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 将一个treenode转换为BFS的list形式
        if not root:
            return '[]'
        # 用队列记录
        from collections import deque
        q = deque()
        q.append(root)
        res = []
        while q:
            temp = q.popleft()
            if temp:
                res.append(str(temp.val))
                q.append(temp.left)
                q.append(temp.right)
            else:
                res.append('null')
        return '[' + ','.join(res) + ']' 

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 遍历data构建二叉树
        if data == '[]':
            return 
        v = str(data[1:-1]).split(',')  
        res,n,i = TreeNode(v[0]),len(v),1,
        from collections import deque
        q = deque()
        q.append(res)
        while q and i<n:
            temp = q.popleft()
            temp.left,temp.right = TreeNode(v[i]),TreeNode(v[i+1])
            q.append(temp.left)
            q.append(temp.right)
            i += 2
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec_2:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'null'
        else:
            return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 遍历data构建二叉树
        data = data.split(',')
        # res = TreeNode(data[0])
        def dfs(data):
            temp = data.pop(0)
            if temp == 'null':
                return None
            res = TreeNode(int(temp))
            res.left = dfs(data)
            res.right = dfs(data)
            return res
        return dfs(data)
        
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))