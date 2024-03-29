class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
                rows,cols=len(matrix),len(matrix[0])
                for i in range(1,rows):matrix[i][0]+=matrix[i-1][0]
                for i in range(1,cols):matrix[0][i]+=matrix[0][i-1]
                for i in range(1,rows):
                    for j in range(1,cols):
                        matrix[i][j]+=matrix[i-1][j]+matrix[i][j-1]-matrix[i-1][j-1]
                self.matrix=matrix
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
                sub1=self.matrix[row1-1][col2] if row1!=0 else 0
                sub2=self.matrix[row2][col1-1] if col1!=0 else 0
                add1=self.matrix[row1-1][col1-1] if row1!=0 and col1!=0 else 0
                return self.matrix[row2][col2]-sub1-sub2+add1