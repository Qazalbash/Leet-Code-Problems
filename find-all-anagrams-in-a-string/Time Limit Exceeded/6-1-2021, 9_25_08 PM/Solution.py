// https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_ = sorted(p)
        m = len(p)
        return [i for i in range(len(s)-m+1) if sorted(s[i:i+m]) == p_]