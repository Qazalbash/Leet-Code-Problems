// https://leetcode.com/problems/simplified-fractions

class Solution:
    def GCD(self, x, y):
        while y:
            x, y = y, x % y
        return abs(x)
    
    def simplifiedFractions(self, n: int) -> List[str]:
        fracs = set()
        p = 1
        for num in range(1, n):
            for denum in range(num+1,n+1):
                # if num < denum:
                p = self.GCD(denum, num)
                fracs.add(f"{num // p}/{denum // p}")
        return list(fracs)
                
        