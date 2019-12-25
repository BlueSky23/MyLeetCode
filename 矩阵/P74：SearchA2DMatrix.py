# 两次二分查找
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        # 确定哪一行
        i, j = 0, len(matrix) - 1
        while i <= j:
            mid = (i + j) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                i = mid + 1
            else:
                j = mid - 1
        # 根据二分查找的特性，有matrix[j]小于target,matrix[i]>target,所以在j行查找
        tmp = j
        i, j = 0, len(matrix[0]) - 1
        while i <= j:
            mid = (i + j) // 2
            if matrix[tmp][mid] == target:
                return True
            elif matrix[tmp][mid] < target:
                i = mid + 1
            else:
                j = mid - 1

        return False
