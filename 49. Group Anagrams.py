class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for i in strs:
            j = "".join(sorted(i))
            ana[j] = ana.get(j, []) + [i]
        return [ana[i] for i in ana.keys()]
