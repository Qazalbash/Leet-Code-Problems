// https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        s = -1
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            s = 1
        divisor = abs(divisor)
        dividend = abs(dividend)
        q = 0
        d = divisor
        while d <= dividend:
            d += divisor
            q+=1
        return q if s == 1 else -q