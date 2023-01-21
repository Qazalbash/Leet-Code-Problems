// https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "*" or p == s:
            return True
        elif p.count("*") == 0:
            if len(p) == len(s):
                pi = 0
                si = 0
                while pi < len(p) and si < len(s):
                    if p[pi] == "?" or s[si] == p[pi]:
                        si += 1
                        pi += 1
                    else:
                        return False
            return False
        pi = 0
        si = 0
        while pi < len(p) and si < len(s):
            if p[pi] == "*":
                pi += 1
                while pi < len(p) and si < len(s) and s[si] != p[pi]:
                    si += 1
        return True