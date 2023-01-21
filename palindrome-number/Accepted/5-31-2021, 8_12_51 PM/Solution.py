// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <= 0 or x > 2 ** 31 - 1 or x < -2 ** 31:
            return x == 0
        N = 0
        m = floor(log(x, 10))
        for k in range(m+1):
            N += 10 ** (m - k) * ((x // 10 ** k) - 10 * (x // 10 ** (k + 1)))
        return int(N) == x