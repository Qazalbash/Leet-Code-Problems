// https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        trib = lambda m: (3*m-m**2)//2 if m < 3 else trib(m-1)+trib(m-2)+trib(m-3)
        return trib(n)