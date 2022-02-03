class Solution:

    def mySqrt(self, x: int) -> int:
        i = 0
        sqrt = 0
        while (i + 1)**2 <= x:
            i += 1
            sqrt += 1
        return sqrt
