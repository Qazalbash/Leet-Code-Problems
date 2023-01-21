// https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hs = lambda string: hash("".join(sorted(string)))
        pHash = hs(p)
        m = len(p)
        return [i for i in range(len(s)-m+1) if hs(s[i:i+m]) == pHash]
        # return [index for index, Hash in enumerate(possible) if pHash == Hash]