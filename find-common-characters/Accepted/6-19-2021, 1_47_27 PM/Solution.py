// https://leetcode.com/problems/find-common-characters

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s={j:[] for j in set("".join(words))}
        for i in words:
            for j in set(i):
                s[j]+=[i.count(j)]
        r=[]
        for k,v in s.items():
            if len(v)==len(words):
                for h in range(min(v)):
                    r.append(k)
        return r