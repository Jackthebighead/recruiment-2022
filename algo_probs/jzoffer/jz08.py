# 题意：旋转数组求最小值
# 解法：不同于O(n)的算法，可以采用二分法进行查找，只不过这不是将mid和target相比较而是将mid和right比，O(lgn)复杂度。
# 常见二分法注释在下面
# O(n)的方法注释在下面

class Solution(object):
    def minArray(self, numbers):
        left, right = 0, len(numbers)-1
        while left<right:
            mid = left + (right-left) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else: 
                right -= 1
        return numbers[left]

# Linear time solution:
# class Solution:
#     def minArray(self, numbers):
#         # input: numbers: List[int]
#         # output: int
#         if not numbers:
#             return 
#         pre = numbers[0]
#         for i in numbers:
#             if pre <= i:
#                 continue
#             else:
#                 return i
#         return pre

# 普遍二分法：在一个递增list中找target相同的数的index
# class Solution:
    # def binarySearch(self, numbers, target):
    #     # input: numbers: List[int]
    #     # output: int
    #     if not numbers:
    #         return -1
    #     left, right = 0, len(numbers)
    #     while left<=right:
    #         mid = left + (right-left) // 2
    #         if numbers[mid] > target:
    #             right = mid - 1
    #         elif numbers[mid] < target:
    #             left = mid + 1
    #         else:
    #             return mid
    #     return -1

# 二分法变式：查找递增(>=)的list中与target相同的最左边的数的index
# class Solution:
    # def binarySearch(self, numbers, target):
    #     # input: numbers: List[int]
    #     # output: int
    #     if not numbers:
    #         return -1
    #     left, right = 0, len(numbers)
    #     while left<=right:
    #         mid = left + (right-left) // 2
    #         if numbers[mid] >= target:  # 改动
    #             right = mid - 1
    #         elif numbers[mid] < target:
    #             left = mid + 1
        
    #     if left > len(numbers) or numbers[left]!=target:  # 改动
    #         return -1
    #     return left

# 二分法变式：查找递增(>=)的list中与target相同的最右边的数的index
# class Solution:
    # def binarySearch(self, numbers, target):
    #     # input: numbers: List[int]
    #     # output: int
    #     if not numbers:s
    #         return -1
    #     left, right = 0, len(numbers)
    #     while left<=right:
    #         mid = left + (right-left) // 2
    #         if number[mid] > target:  # 改动
    #             right = mid - 1
    #         elif numbers[mid] <= target:
    #             left = mid + 1
        
    #     if right < 0 or numbers[right]!=target:  # 改动
    #         return -1
    #     return right