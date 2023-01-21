// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # pow=lambda a,b: 1 if b==0 else a*pow(a,b-1)
        # x=(n>0)*x+(n<0)/x
        # return pow(x,abs(n))
        return x ** n