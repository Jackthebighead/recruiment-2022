# Why this recursion works for 二叉树的镜像问题。 https://www.nowcoder.com/practice/a9d0ecbacef9410ca97463e4a5c83be7?tpId=188&tqId=38075&rp=1&ru=%2Factivity%2Foj&qru=%2Fta%2Fjob-code-high-week%2Fquestion-ranking&tab=answerKey？
# There are obviously multiple 。 Or the program just read the variable pRoot regardless of the output of solution？

class Solution:
    def Mirror(self , pRoot ):
        # write code here
        if not pRoot:
            return None
        pRoot.left, pRoot.right = pRoot.right, pRoot.left
        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)
        return pRoot

class Solution_mine:
    def Mirror(self , pRoot ):
        # write code here
        if not pRoot: return 
        def recur(pRoot):
            if not pRoot: return 
            pRoot.left,pRoot.right = pRoot.right,pRoot.left
            recur(pRoot.left)
            recur(pRoot.right)
        recur(pRoot)
        return pRoot