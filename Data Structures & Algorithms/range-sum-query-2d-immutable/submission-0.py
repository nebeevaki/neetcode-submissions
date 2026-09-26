class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = self.create_prefix(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1 
        if col1 == 1:
            return self.prefix[row2][col2] - self.prefix[row1 - 1][col2]
        elif row1 == 1:
            return self.prefix[row2][col2] - self.prefix[row2][col1 - 1]
        else:
            return (self.prefix[row2][col2]
             - self.prefix[row2][col1 - 1]
             - self.prefix[row1 - 1][col2]
             + self.prefix[row1 - 1][col1 - 1]
            )

        
    def create_prefix(self, matrix):
        row = len(matrix) + 1
        col = len(matrix[0]) + 1
        prefix = [[0] * (col) for _ in range(row)]
        for i in range(1, row):
            for j in range(1, col):
                prefix[i][j] = self.matrix[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

        return prefix
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
