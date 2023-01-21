// https://leetcode.com/problems/smallest-even-multiple

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        lcm = n if n > 2 else 2
        while (lcm % n) or (lcm % 2):
            lcm += 1
        return lcm
        