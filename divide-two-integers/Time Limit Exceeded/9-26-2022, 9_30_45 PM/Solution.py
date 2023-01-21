// https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        q = 0
        d = abs(divisor)
        while d <= dividend:
            d += divisor
            q+=1
        return q if divisor > 0 else -q