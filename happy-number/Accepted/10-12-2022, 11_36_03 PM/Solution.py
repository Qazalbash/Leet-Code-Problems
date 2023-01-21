// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 9:
            d = 0
            while n:
                d += (n % 10) ** 2
                n = n // 10
            n = d
        return (n == 1) or (n == 7)

