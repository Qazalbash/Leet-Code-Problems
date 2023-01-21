// https://leetcode.com/problems/percentage-of-letter-in-string

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if letter not in s:
            return 0
        n = len(s)
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        return int(d[letter]/n*100)