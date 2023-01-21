// https://leetcode.com/problems/largest-odd-number-in-string

class Solution:
    def largestOddNumber(self, num: str) -> str:
        r = len(num) - 1
        while not(int(num[r]) % 2) and r >= 0:
            r -= 1
        return num[:r + 1]
        