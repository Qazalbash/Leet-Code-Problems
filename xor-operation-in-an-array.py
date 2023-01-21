// https://leetcode.com/problems/xor-operation-in-an-array

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        r = start
        for i in range(1, n):
            r ^= start + 2 * i
        return r