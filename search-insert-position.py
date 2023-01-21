// https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while True:
            mid = (low+high)//2
            if low>high:
                return low
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            elif nums[mid] > target:
                high=mid-1