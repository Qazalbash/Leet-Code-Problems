// https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        trib = lambda m: m if m < 2 else (1 if m == 2 else trib(m-1)+trib(m-2)+trib(m-3))
        return trib(n)