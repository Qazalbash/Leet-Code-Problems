// https://leetcode.com/problems/contains-duplicate-iii

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and abs(i - j) <= indexDiff and abs(nums[i] - nums[j]) <= valueDiff:
                    return True
        return False