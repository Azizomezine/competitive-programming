class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        top = 0
        bottom = len(matrix) - 1
        searchRow = 0

        while top <= bottom:
            row = (top + bottom)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                searchRow = row
                break
        
        
        if not(top <= bottom):
            return False

        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = (left + right)//2
            if target < matrix[searchRow][mid]:
                right = mid - 1
            elif target > matrix[searchRow][mid]:
                left = mid + 1
            else:
                return True
        return False