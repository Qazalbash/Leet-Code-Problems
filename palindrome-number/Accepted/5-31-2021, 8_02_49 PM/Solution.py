// https://leetcode.com/problems/palindrome-number

from math import log, floor
class Solution:
    def digit(self, n, i):
        return floor(n/10**i) - 10 * floor(n/10**(i+1))
    
    def isPalindrome(self, x: int) -> bool:
        num = [i for i in str(x)]
        return num == num[::-1]