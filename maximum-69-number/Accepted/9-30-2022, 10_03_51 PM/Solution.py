// https://leetcode.com/problems/maximum-69-number

class Solution:
    def maximum69Number (self, num: int) -> int:
        r = 0
        for i in range(3, -1, -1):
            d = (num // 10 ** i) - 10*(num // 10 ** (i+1)) 
            if d == 6:
                r += 9 * 10 ** i + num % 10 ** i
                break
            r += d * 10 ** i
        return r