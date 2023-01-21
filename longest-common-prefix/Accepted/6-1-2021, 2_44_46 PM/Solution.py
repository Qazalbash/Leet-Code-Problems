// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        strs = sorted(strs)
        for i in range(len(strs[0])):
            if all(strs[0][i] == j[i] for j in strs[1:]):
                result += strs[0][i]
            else:
                break
        return result