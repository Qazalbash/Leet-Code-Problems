// https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = set(range(len(nums)+1)) - set(nums)
        return m.pop()