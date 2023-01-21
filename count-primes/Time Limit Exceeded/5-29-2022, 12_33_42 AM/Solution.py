// https://leetcode.com/problems/count-primes

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        p = 2
        count = 1
        nums = set(range(2,n))
        while p * p < n:
            for i in range(p*p, n, p):
                nums -= set([i])
            p += 1
            while p not in nums:
                p += 1
        return len(nums)
        