// https://leetcode.com/problems/sort-characters-by-frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1

        d = sorted(list(d.items()), key=lambda k: k[1], reverse=True)
        
        r = ""
        for i, j in d:
            r += i * j
        return r
        