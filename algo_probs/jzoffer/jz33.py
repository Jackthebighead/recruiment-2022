# 题意：二叉搜索树的后序遍历。输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
# 题解1: 用递归。二叉搜索树的特性是left<val<right，后序遍历的特性是：小，大，自己，根据这个特性从倒数找出左儿子右儿子，且左儿子到右儿子之间都大于，右儿子到倒数都小于才能接着递归。
# 那么唯一不同的，比较复杂的是将整个list作为递归，更节省的是用指针来递归
# 题解2: 用单调栈来解决。利用树后续遍历节点的关系，对于后序遍历倒序list（自己，大，小），r_i后面的节点r_x，r_i的父节点为root，只可能为以下两种情况：
# ① r_x为 r_i的左、右子树的各节点；
# ② r_x为 root 的父节点或更高层父节点的左子树的各节点。
# 在二叉搜索树中，以上节点都应小于 root。对于一个后序遍历倒序，若一直递增则一直有右子树，若出现递减则需要判断递减之后的是否符合，即当出现递减的时候需要找到root，然后来判断
# 所以，对一个后序遍历倒序list我们可以维护一个递增栈来找root，通过判断后续节点是否大于root来判断是否符合后序遍历。
# root为什么能找到？因为我们维护一个单增栈且while的条件是当前值小于栈顶则弹出至当前值大于栈顶（或栈为空），因此最后一个弹出的一定是该节点的直接root（root的root<该节点<root）
# 而一个后续遍历，当前值小于root且当前值的后面都得小于root，若不符合则False。初始化root为float('+inf')


class Solution:
    def verifyPostorder(self, postorder):
        # inputs: postorder: List[int]
        # outputs: bool
        def recur(postorder):
            if not postorder:
                return True
            r = len(postorder)-2
            val = postorder[-1]
            while postorder[r]>val:
                r -= 1
            l = r
            while postorder[l]<val:
                l -= 1
            if l < 0:
                return recur(postorder[:l+1]) and recur(postorder[l+1:-1])
            else:
                return False
        return recur(postorder)

class Solution_2:
    def verifyPostorder(self, postorder):
        # inputs: postorder: List[int]
        # outputs: bool
        # l,r记录区间
        def recur(l,r):
            if l>=r:
                return True
            # 从最左边开始好，从右边减j可能为-1会越出边界
            i = l
            while postorder[i]<postorder[r]: i += 1
            j = i
            while postorder[j]>postorder[r]: j += 1
            return j==r and recur(l,i-1) and recur(i,r-1)
        return recur(0,len(postorder)-1)

class Solution_3:
    def verifyPostorder(self, postorder):
        # inputs: postorder: List[int]
        # outputs: bool
        stack, root = [], float('+inf')
        for i in range(len(postorder)-1,-1,-1):
            # 若当前值小于当前的root，则不符合后序遍历特征
            if postorder[i]>root:
                return False
            # 维护一个单调递增栈，目的是找出单调递减的那一个数字，从而导出root，进行比较
            while stack and postorder[i]<stack[-1]:
                root = stack.pop()
            stack.append(postorder[i])
        return True
        
        


        
