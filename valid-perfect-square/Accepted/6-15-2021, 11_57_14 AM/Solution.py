// https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if 1<=num<=2**31-1:
            return int(num**0.5)**2==num