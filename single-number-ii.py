// https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        retard = set()
        potential = set()
        for i in nums:
            if i in potential:
                potential.remove(i)
                retard.add(i)
            elif i in retard:
                continue
            else:
                potential.add(i)
        return potential.pop()