// https://leetcode.com/problems/find-greatest-common-divisor-of-array

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x = float("inf")
        y = 0
        for n in nums:
            if n < x:
                x = n
            if y < n:
                y = n
        while y:
            x, y = y, x % y
        return x
