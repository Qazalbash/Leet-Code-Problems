// https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        one = 0
        for i in range(32):
            one += n//(1<<i) - 2*(n//(1<<i+1))
        return one