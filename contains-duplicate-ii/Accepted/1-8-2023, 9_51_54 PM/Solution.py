// https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], []) + [i]
        for key, value in d.items():
            if len(value) > 1:
                for j in range(len(value)-1):
                    if value[j+1] <= k + value[j]:
                        return True
        return False