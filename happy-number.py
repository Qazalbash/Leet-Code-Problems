// https://leetcode.com/problems/happy-number

class Solution:
    @staticmethod
    def sqSum(n: int) -> int:
        s = 0
        while n:
            s += (n % 10) ** 2
            n = n // 10
        return s
    
    def isHappy(self, n: int) -> bool:
        while n > 9:
            n = self.sqSum(n)
        return (n == 1) or (n == 7)

