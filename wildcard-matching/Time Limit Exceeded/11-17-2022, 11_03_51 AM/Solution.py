// https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "*" or p == s:
            return True
        pi = 0
        si = 0
        
        while pi < len(p) and si < len(s):
            if p[pi] == "*":
                while s[si] != p[pi+1]:
                    si += 1
            elif p[pi] == "?":
                if s[si] == p[pi]:
                    pi += 1
                    si += 1
                else:
                    return False
            else:
                if s[si] == p[pi]:
                    pi += 1
                    si += 1
                else:
                    return False