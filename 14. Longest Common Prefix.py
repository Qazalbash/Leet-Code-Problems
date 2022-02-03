class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        result, strs = "", sorted(strs)
        index = 0
        for i in strs[0]:
            if all(i == j[index] for j in strs[1:]):
                result += i
            else:
                break
            index += 1
        return result
