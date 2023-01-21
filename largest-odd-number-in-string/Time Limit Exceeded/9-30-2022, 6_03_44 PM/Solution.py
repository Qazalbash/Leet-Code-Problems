// https://leetcode.com/problems/largest-odd-number-in-string

class Solution:
    def largestOddNumber(self, num: str) -> str:
        k = None
        n = len(num)
        r = n-1

        # for i in range(n-1, -1, -1):
        #     if int(num[i]) % 2:
        #         break
        #     r = i
        
        while int(num[r]) % 2 == 0 and r > 0:
            r -= 1

        num = num[:r+1]
        n = r+1
        r = 0

        for j in range(n):
            for i in range(n, 0, -1):
                k = int(num[j:i+j])
                if k % 2 and r < k:
                    r = k
            if r:
                return str(r)
        if r:
            return str(r)
        return ""