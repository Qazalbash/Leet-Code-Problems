// https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        maxPens = total // cost1
        count = 0
        for i in range(maxPens+1):
            # maxPencil = (total - i * cost1) // cost2
            count += (total - i * cost1) // cost2 + 1
        return count