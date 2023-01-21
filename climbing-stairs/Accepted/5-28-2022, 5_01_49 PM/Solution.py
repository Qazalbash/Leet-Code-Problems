// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        phi = (1+5**0.5)/2
        f = (int)((phi ** (n + 1) - ( -phi ) ** ( -n - 1 ) ) / (5 ** 0.5))
        return f