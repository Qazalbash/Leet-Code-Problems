class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(num ** 0.5) ** 2 == num
