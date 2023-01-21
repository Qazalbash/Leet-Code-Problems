// https://leetcode.com/problems/remove-stones-to-minimize-the-total

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = len(piles) - 1
        for _ in range(k):
            piles.sort()
            piles[n] = piles[n] - piles[n]//2
        return sum(piles)