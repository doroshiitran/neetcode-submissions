class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # mid_row = len (for _ in nums)
        # mid_col = len(matrix)
        # mid = (mid_row, mid_col)
        # if target > matrix[mid] start from the matrix[mid] to the right and opposite
        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = row * col -1
        while left <= right:
            mid = (left + right) //2
            current_row = mid // col
            current_col = mid % col

            value = matrix[current_row][current_col]
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False