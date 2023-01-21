// https://leetcode.com/problems/percentage-of-letter-in-string

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if letter not in s:
            return 0
        n = len(s)
        d = s.count(letter)
        return int(d*100/n)