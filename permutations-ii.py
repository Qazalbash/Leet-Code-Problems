// https://leetcode.com/problems/permutations-ii

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        p = list(permutations(nums))
        f = []
        for i in p:
            if i not in f:
                f.append(i)
        return f