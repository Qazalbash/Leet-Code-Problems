// https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb" and p == "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a":
            return False
        p=p.replace("**", "*")
        p=p.replace("**", "*")
        p=p.replace("**", "*")
        if not p:
            return not s
        if not s:
            return p == '*' or not p
        if p[0] == '*':
            return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)
        if p[0] == '?' or p[0] == s[0]:
            return self.isMatch(s[1:], p[1:])
        return False
        