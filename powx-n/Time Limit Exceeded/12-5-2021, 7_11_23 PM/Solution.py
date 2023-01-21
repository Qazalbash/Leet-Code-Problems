// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            x = 1/x
            n = abs(n)
        
        return self.myPow(x,n-n//2) * self.myPow(x,n//2)