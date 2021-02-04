# 题意：机器人运动范围，遇到某个限定条件就不能走，求出能走的所有点的数量
# 解法1：DFS，用暴力循环（2个for）来模拟机器人要走的每一条路。用visited存储满足条件的点坐标。
# 解法2：BFS，用一个队列存放广度优先的buffer，用给一个visited set存放可以的点，依次弹出buffer中的点，然后向右或者向下走，若符合条件就加入visited set，不符合就接着往下BFS。

# 深度优先解法
class Solution:
    def movingCount(self, m, n, k):
        # input: m: int, n: int, k: int
        # output: int
        def char_sum(i):
            res = 0
            while i!=0:
                res += i%10
                i = i // 10
            return res
        visited = set([(0,0)])
        for i in range(m):
            for j in range(n):
                if ((i-1,j) in visited or (i,j-1) in visited) and (char_sum(i)+char_sum(j)<=k):
                    visited.add((i,j))
        return len(visited)

# 广度优先解法
class Solution_2:
    def count_sum(self, i):
        res = 0
        while i:
            res += i%10
            i //= 10
        return res

    def movingCount(self, m, n, k):
        # 广度遍历
        visited = set()
        queue = [(0,0)]
        while queue:
            i,j = queue.pop(0)
            if (self.count_sum(i)+self.count_sum(j))<=k and i<m and j<n and (i,j) not in visited:
                visited.add((i,j))
                queue.append((i+1,j))
                queue.append((i,j+1))
        return len(visited)
            


