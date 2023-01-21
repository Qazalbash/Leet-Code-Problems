// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num:
            num = (num >> 1) * ( 1 - num % 2 ) + ( num - 1 ) * (num % 2)
            count += 1
        return count
