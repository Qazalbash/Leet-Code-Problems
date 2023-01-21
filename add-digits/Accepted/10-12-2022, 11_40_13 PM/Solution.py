// https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, n: int) -> int:
        while n > 9:
            d = 0
            while n:
                d += n % 10
                n = n // 10
            n = d
        return n

