// https://leetcode.com/problems/most-frequent-even-element

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i % 2 == 0:
                d[i] = d.get(i, 0) + 1
        if d:
            r = max(d.values())
            return min([i for i in d.keys() if d[i] == r])
        return -1