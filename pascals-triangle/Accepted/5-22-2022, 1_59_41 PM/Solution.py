// https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = [[1 for _ in range(j)] for j in range(1, numRows + 1)]
        for i in range(2, numRows):
            for j in range(1, i):
                final[i][j] = final[i - 1][j - 1] + final[i - 1][j]
        return final