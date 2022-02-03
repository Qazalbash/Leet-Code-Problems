class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        if 0 <= c <= 2**31 - 1:
            i = 0
            while c >= i**2:
                if int((c - i**2)**0.5)**2 + i**2 == c:
                    return True
                i += 1
            return False
