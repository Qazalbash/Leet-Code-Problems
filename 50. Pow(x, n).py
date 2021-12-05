class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, abs(n))
        else:
            return x * self.myPow(x, n - 1) if n % 2 else self.myPow(x * x, n // 2)
