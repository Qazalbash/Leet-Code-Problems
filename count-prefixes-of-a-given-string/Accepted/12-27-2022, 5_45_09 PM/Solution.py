// https://leetcode.com/problems/count-prefixes-of-a-given-string

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for i in words:
            n = len(i)
            if s[:n] == i:
                count += 1
        return count