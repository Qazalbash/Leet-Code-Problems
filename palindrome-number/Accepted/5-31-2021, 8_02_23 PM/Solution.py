// https://leetcode.com/problems/palindrome-number

from math import log, floor
class Solution:
    def digit(self, n, i):
        return floor(n/10**i) - 10 * floor(n/10**(i+1))
    
    def isPalindrome(self, x: int) -> bool:
        if x <= 0:
            return x == 0
        num = [i for i in str(x)]
        return num == num[::-1]
        # return all([i == j for i, j in zip(num, num[::-1])])
        # m = floor(log(abs(x), 10))
        # if x < -2**31 or x > 2 ** 31 - 1:
        #     return False
        # for i in range(floor(m/2)):
        #     if self.digit(x, m - i) != self.digit(x, i):
        #         return False
        # return True