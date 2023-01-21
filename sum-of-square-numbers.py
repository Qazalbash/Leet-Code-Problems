// https://leetcode.com/problems/sum-of-square-numbers

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=0
        while c-i**2>=0:
            if int((c-i**2)**0.5)**2+i**2==c:
                return True
            i+=1
        return False