// https://leetcode.com/problems/largest-odd-number-in-string

class Solution:
    def largestOddNumber(self, num: str) -> str:
        r = 0
        n = len(num)
        k = None
        for j in range(n):
            # for i in range(1,n+1):
            for i in range(n, 0, -1):
                k = int(num[j:i+j])
                if k % 2 and r < k:
                    r = k
        if r:
            return str(r)
        return ""