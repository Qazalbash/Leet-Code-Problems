// https://leetcode.com/problems/palindrome-number

class Solution:
    def reverse(self, x: int) -> int:
        if x <= 0 or x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        N = 0
        m = floor(log(x, 10))
        for k in range(m+1):
            N += 10 ** (m - k) * (floor(x / 10 ** k) - 10 * floor(x / 10 ** (k + 1)))
        return N * (- 2 ** 31 <= N <= 2 ** 31 - 1)
    
    def isPalindrome(self, x: int) -> bool:
        return self.reverse(x) == x