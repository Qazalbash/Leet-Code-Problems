// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = set()
        for i in nums:
            if i in unique:
                unique.remove(i)
            else:
                unique.add(i)
        return unique.pop()
        