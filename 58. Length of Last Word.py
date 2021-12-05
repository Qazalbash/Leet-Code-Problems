class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l, s = 0, s.strip(" ")
        for i in s:
            l = (l + 1) * (i != " ")
        return l
