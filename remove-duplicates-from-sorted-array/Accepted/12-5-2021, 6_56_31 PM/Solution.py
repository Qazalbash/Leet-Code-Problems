// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = set()
        for i in nums:
            result.add(i)
        nums[:] = sorted(list(result))