# 题意：从上到下打印二叉树3: 奇数层从左到右，偶数层从右到左
# 题解1: 辅助双端队列
# 题解2: 对奇偶不同处理，若该层的res_temp的len为奇数则正序加入res，若为偶数则倒序加入res。
# 题解3: 对单数双数层不同处理，这个最笨。if 即可。
# res.append(tmp[::-1] if len(res) % 2 else tmp)

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
        res,queue,cnt = [], collections.deque(),1
        queue.append(root)
        while queue:
            res_temp = collections.deque()
            for _ in range(len(queue)):
                temp = queue.popleft()
                # 将res_temp也设置为双端队列，偶数层就插入到左边
                if cnt % 2: 
                    res_temp.append(temp.val)
                else:
                    res_temp.appendleft(temp.val)
                # 双端队列左边出右边进
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            res.append(list(res_temp))
            cnt += 1
        return res