// https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, m: int) -> List[int]:
        def hammingWeight(n: int) -> int:
            one = 0
            for i in range(32):
                one += n // (1 << i) - 2 * (n // ( 1 << i + 1))
            return one
        return [hammingWeight(i) for i in range(m+1)]