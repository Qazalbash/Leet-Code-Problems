class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row, col = len(matrix), len(matrix[0])
        pd = set([matrix[i][i] for i in range(row) if i < col])
        d = [pd]
        for j in range(1, row):
            d.append(set([matrix[i + j][i] for i in range(row - j) if i < col]))
        for j in range(1, col):
            d.append(set([matrix[i][i + j] for i in range(col - j) if i < row]))
        return all(len(i) == 1 for i in d)
