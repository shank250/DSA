class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_ = 0
        n = len(matrix)
        for i in range(1, n):
            for j in range(1, n):
                if matrix[i - 1][j] == matrix[i][j - 1] and matrix[i - 1][j - 1] == matrix[i - 1][j] and  matrix[i - 1][j - 1]  ==  matrix[i][j - 1]:
                    matrix[i][j] == 1 + matrix[i][j - 1]
                    max_ = max(max, matrix[i][j])
