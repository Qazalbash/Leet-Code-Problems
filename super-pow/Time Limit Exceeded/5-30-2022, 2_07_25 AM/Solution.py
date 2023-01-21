// https://leetcode.com/problems/super-pow

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        r = (a ** b[-1]) % 1337
        for i in range(-2, -len(b)-1, -1):
            c = (a % 1337) ** (b[i] * 10 ** (-i-1)) 
            r = (r * c % 1337) % 1337
        return r