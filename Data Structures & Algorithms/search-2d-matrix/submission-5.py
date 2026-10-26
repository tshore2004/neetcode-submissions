class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        rowLen = len(matrix[0])
        right = len(matrix) * rowLen - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // rowLen
            col = mid % rowLen
            if matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                return True

        return False