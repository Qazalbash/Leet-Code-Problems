// https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, m: int) -> List[int]:
        final = [0]
        for n in range(1, m+1):
            one = 0
            for i in range(17):
                one += n // (1 << i) - 2 * (n // ( 1 << i + 1))
            final.append(one)
        return final