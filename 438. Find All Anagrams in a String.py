class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_ = sorted(p)
        m = len(p)
        result = []
        for i in range(len(s) - m + 1):
            if sorted(s[i:i + m]) == p_:
                result.append(i)
        return result
