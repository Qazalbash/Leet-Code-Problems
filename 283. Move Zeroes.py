class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = 0
        for i in nums:
            zeros += i == 0
        nums[:] = [j for j in nums if j != 0] + [0] * zeros
