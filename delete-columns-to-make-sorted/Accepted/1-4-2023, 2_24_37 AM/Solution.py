// https://leetcode.com/problems/delete-columns-to-make-sorted

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        n = len(strs) - 1
        for i in range(len(strs[0])):
            count += not all(strs[t][i] <= strs[t+1][i] for t in range(n))
        return count