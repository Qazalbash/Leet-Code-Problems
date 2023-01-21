// https://leetcode.com/problems/permutation-in-string

from itertools import permutations as perm
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        pS1 = list(perm(s1))
        possible = [tuple(s2[i:i+m]) for i in range(len(s2)-m+1)]
        for j in pS1:
            if j in possible:
                return True
        return False