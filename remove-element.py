// https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        for i in nums:
            if i != val:
                temp.append(i)
        nums[:] = temp