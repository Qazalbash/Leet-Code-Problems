// https://leetcode.com/problems/simplified-fractions

class Solution:
    def GCD(self, x, y):
        while y:
            x, y = y, x % y
        return abs(x)
    
    def simplifiedFractions(self, n: int) -> List[str]:
        fracs = set()
        p = 1
        for denum in range(2,n+1):
            for num in range(1, n):
                if num < denum:
                    p = self.GCD(denum, num)
                    fracs.add(f"{num // p}/{denum // p}")
        return list(fracs)
                
        