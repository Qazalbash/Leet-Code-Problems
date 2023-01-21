// https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return int((3*n-n**2)/2)
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)