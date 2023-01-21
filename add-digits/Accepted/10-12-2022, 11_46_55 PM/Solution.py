// https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 9 * (num % 9 == 0) + (num % 9) * (num % 9 != 0)