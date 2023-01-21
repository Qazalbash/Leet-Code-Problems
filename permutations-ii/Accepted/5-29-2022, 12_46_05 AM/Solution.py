// https://leetcode.com/problems/permutations-ii

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        f = []
        for i in list(permutations(nums)):
            if i not in f:
                f.append(i)
        return f