// https://leetcode.com/problems/gray-code

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        seq_small = self.grayCode(n - 1)
        return seq_small + [2 ** (n - 1) + i for i in seq_small[::-1]]