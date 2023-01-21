// https://leetcode.com/problems/power-of-two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n%2 == 0:
            n //= 2
        if n == 1:
            return True
        return False