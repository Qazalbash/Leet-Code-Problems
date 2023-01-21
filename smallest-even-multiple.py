// https://leetcode.com/problems/smallest-even-multiple

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        greater = n if n > 2 else 2
        while (greater % n != 0) or (greater % 2 != 0):
            greater += 1
        return greater
        