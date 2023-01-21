// https://leetcode.com/problems/perfect-number

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sigma = 0
        for i in range(1,num//2+1):
            sigma += i * (num % i == 0)
        return sigma == num