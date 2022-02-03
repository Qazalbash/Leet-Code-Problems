class Solution(object):

    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return [j, i]
