// https://leetcode.com/problems/rotate-function

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        F_max = 0
        for _ in range(len(nums)):
            F = 0
            for i, j in enumerate(nums):
                F += i * j
            if F_max < F:
                F_max = F
            nums = [nums[-1]]+nums[:-1]
        return F_max
            