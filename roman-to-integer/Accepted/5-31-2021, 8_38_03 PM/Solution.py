// https://leetcode.com/problems/roman-to-integer

from collections import Counter
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res, tmp = 0, 0
        for i in reversed(s):
            res += dic[i] * (1 * (dic[i]>=tmp) - 1 * (dic[i]<tmp))
            # if dic[i]>=tmp:
            #     res=res+dic[i]
            # else:
            #     res=res-dic[i]
            tmp=dic[i]
        return res
        # conv = {"I": 1, "$": 4, "%": 9, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # if "IV" in s:
        #     s = s.replace("IV", "$")
        # if "IX" in s:
        #     s = s.replace("IX", "%")
        # result = 0
        # count = Counter(s)
        # for key, value in count.items():
        #     result += value * conv[key]
        # return result * (0 < result < 4000) * (0 < len(s) < 16)