// https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        import numpy as np
        nums[:] = np.sort([t*t for t in nums])
        # nums = np.sort(nums)
        return [i for i in nums]