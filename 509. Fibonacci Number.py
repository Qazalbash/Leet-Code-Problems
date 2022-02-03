class Solution:

    def fib(self, n: int) -> int:
        f = lambda n: n if n < 2 else f(n - 1) + f(n - 2)
        return f(n)
