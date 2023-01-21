// https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "*" or p == s:
            return True
        elif p.count("*") == 0:
            if len(p) != len(s):
                return False
        pi = 0
        si = 0
        while pi < len(p) and si < len(s):
            if p[pi] == "*":
                pi += 1
                while pi < len(p) and si < len(s):
                    if s[si] == p[pi]:
                        return self.isMatch(s[si:], p[pi-1:])
                    si += 1
            elif p[pi] == "?" or s[si] == p[pi]:
                pi += 1
                si += 1
            else:
                return False
        return True