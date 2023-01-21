// https://leetcode.com/problems/delete-columns-to-make-sorted

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        # n = len(strs[0])
        # d = {
        #     i : strs[0][i] for i in range(n)
        # }
        # for i in d.keys():
        #     for t in strs[1:]:
        #         if d[i] <= t[i]:
        #             d[i] = t[i]
        #         else:
        #             count += 1
        #             d[i] = "Z"
        for i in range(len(strs[0])):
            # print([strs[t][i] <= strs[t+1][i] for t in range(len(strs)-1)])
            count += not all(strs[t][i] <= strs[t+1][i] for t in range(len(strs)-1))
        return count