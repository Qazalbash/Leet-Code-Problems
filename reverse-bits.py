// https://leetcode.com/problems/reverse-bits

class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(32):
            r += ( n // (1<<i) - 2 * (n // (1 << i + 1))) * (1 << 31 - i)
        return r