// https://leetcode.com/problems/reverse-integer

from math import log, floor
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        sign = (x>0)-(x<0)
        N, x = 0, abs(x)
        m = floor(log(x, 10))
        for k in range(m+1):
            N += 10 ** (m - k) * (floor(x / 10 ** k) - 10 * floor(x / 10 ** (k + 1)))
        return N * sign * (- 2 ** 31 <= N <= 2 ** 31 - 1)