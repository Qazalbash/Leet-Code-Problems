// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = {}
        index=[]
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
            if count[nums[i]]>2:
                index.append(i)
        for j in index[::-1]:
            del nums[j]