// https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        t = lambda m: int((3*m-m**2)/2) if m < 3 else t(m-1)+t(m-2)+t(m-3)
        return t(n)