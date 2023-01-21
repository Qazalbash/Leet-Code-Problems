// https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res, tmp = 0, 0
        for i in reversed(s):
            res += dic[i] * (1 * (dic[i]>=tmp) - 1 * (dic[i]<tmp))
            tmp=dic[i]
        return res