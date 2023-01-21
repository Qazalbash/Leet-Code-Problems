// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if (100.0 < x < 100.0 or -10**4 <= x <= 10**4) and -2**31 <= n <= 2**31-1:
        if n == 0:
            return 1
        elif n < 0:
            return 1/self.myPow(x,abs(n))
        else:
            return x * self.myPow(x, n - 1) if n % 2 else self.myPow(x * x, n // 2)