# 题意：在一个自左向右递增，自下向上递增的数组中是否存在target数字

class Solution:
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

