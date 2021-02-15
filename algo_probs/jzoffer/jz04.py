# 题意：在一个自左向右递增，自下向上递增的数组中是否存在target数字
# 解法1：根据数组特性，从左下角开始，若值小于target，不在这一列，往右边移；若大于，不在这一行可能在这一列，往上走，直到越界。linear time复杂度。
# 解法2：暴力求解，两个for，n^2时间复杂度

class Solution:
    # 解法1
    def findNumberIn2DArray(self, matrix, target):
    # input: matrix: List[List[int]],target: int -> 
    # output: bool
        if not matrix:
            return False
        row = len(matrix) - 1 
        col = len(matrix[0]) - 1
        i = row
        j = 0
        flag = False
        while(i>=0 and j<=col):
            if target > matrix[i][j]:
                j += 1
            elif target < matrix[i][j]:
                i -= 1
            else: 
                flag = True
                return flag
        return flag 

if __name__ == '__main__':
    sol = Solution()
    print(sol.findNumberIn2DArray(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))

