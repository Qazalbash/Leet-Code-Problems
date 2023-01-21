// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        d = sorted(list(d.items()), key=lambda k: k[1], reverse=True)
        return [i[0] for i in d[:k]]