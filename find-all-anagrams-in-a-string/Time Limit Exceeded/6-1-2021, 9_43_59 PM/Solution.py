// https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hs = lambda string: hash("".join(sorted(string)))
        pH = hs(p)
        m = len(p)
        possible = [hs(s[i:i+m]) for i in range(len(s)-m+1)]
        return [I for I, H in enumerate(possible) if pH == H]