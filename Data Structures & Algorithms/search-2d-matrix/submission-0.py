class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # mid_row = len (for _ in nums)
        # mid_col = len(matrix)
        # mid = (mid_row, mid_col)
        # if target > matrix[mid] start from the matrix[mid] to the right and opposite
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == target:
                    return True
        return False