// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (100.0 < x < 100.0 or -10**4 <= x <= 10**4) -2**31 <= n <= 2**31-1:
            if n == 0:
                return 1
            elif n == 1:
                return x
            elif n < 0:
                x = 1/x
                n = abs(n)
                return self.myPow(x,n-n//2) * self.myPow(x,n//2)
            else:
                return self.myPow(x,n-n//2) * self.myPow(x,n//2)