# 题意：判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
# 解法：DFS+pruning。在主函数中，用两个for遍历整个数组，每一个matrix[i][j]为头节点开始dfs，当dfs返回true的时候返回ture。
#      dfs是一个递归函数，传入ij以及一个记录比较到字符串字符的位置k，首先需判断边界条件，若ij不在边界内返回false，其次判断是否与字符串的第一个字符相同，不相同返回false（剪枝）
#      若满足，再判断k是否位于最后一位，若是说明全部匹配返回True
#      若还没完全匹配，先设置该点的值为''（避免重复计算），计算res=（上一点的def） or （下一点的dfs） or （左一点的dfs） or （右一点的dfs），计算完恢复该带你的值为word[k]（因为此时是匹配相同的），然后返回res即可


class Solution:
    def exist(self, board, word):
        # input: board: List[List[str]], word: str
        # output: bool
        def dfs(i,j,k):
            if not (0<=i<len(board)) or not (0<=j<len(board[0])) or not (board[i][j]==word[k]):
                return False
            elif k == len(word)-1:
                return True
            else:
                board[i][j] = ''
                res = dfs(i-1,j,k+1) or dfs(i+1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
                board[i][j] = word[k]
                return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False

    # 非递归dfs
    # def exist_1(self, board: List[List[str]], word: str) -> bool:
    #     # 预处理
    #     w_l = len(word)
    #     if w_l < 1:
    #         return True
    #     rows = len(board)
    #     cols = len(board[0])
    #     # 标记数组
    #     board_vis = [[0] * cols for i in range(rows)]
    #     # 方向数组
    #     dir_list = [[-1, 0], [0, 1], [1, 0],[0, -1]]
    #     # 非递归DFS要用栈维护哦，先把所有头节点放进来，每个节点包括3个值（i,j,l）,i和j是它的坐标，l是它在word中的下标
    #     word_stack = []
    #     for i in range(rows):
    #         for j in range(cols):
    #             if board[i][j] == word[0]:
    #                 word_stack.append((i, j, 0))
    #     # 正式开始DFS咯
    #     while len(word_stack) > 0:
    #         # 获取头节点信息，先不要弹出
    #         top = word_stack[-1]
    #         tx = top[0]
    #         ty = top[1]
    #         tl = top[2]
    #         # 访问这个节点，并开始深度遍历
    #         board_vis[tx][ty] = 1
    #         # 出口条件，如果word遍历完，返回True
    #         if tl == w_l - 1:
    #             return True
    #         # flag记录是否能够继续深度遍历
    #         flag = True
    #         for di in dir_list:
    #             next_x = tx + di[0]
    #             next_y = ty + di[1]
    #             # 深度遍历的条件
    #             if next_x >= 0 and next_x < rows and next_y >= 0 and next_y < cols \
    #                     and board_vis[next_x][next_y] == 0 and board[next_x][next_y] == word[tl + 1]:                   
    #                 # 注意子节点与父节点的关系
    #                 word_stack.append((next_x, next_y, tl + 1))
    #                 flag = False
    #         # 如果不能继续深度遍历，回溯，这个回溯有点复杂：需要一层一层往上回溯，回溯到有多个子节点的地方，类似于树的深度遍历
    #         if flag:
    #             while len(word_stack):
    #                 top = word_stack[-1]
    #                 if top[2] != tl:
    #                     break
    #                 tl -= 1
    #                 # 弹出，并标记取消
    #                 word_stack.pop()
    #                 board_vis[top[0]][top[1]] = 0
    #     return False
