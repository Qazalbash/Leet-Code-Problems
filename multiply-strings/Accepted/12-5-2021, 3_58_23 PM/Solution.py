// https://leetcode.com/problems/multiply-strings

class Solution(object):
    def multiply(self, num1, num2):
        number = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        answer = 0
        m1 = len(num1)
        m2 = len(num2)
        for i in range(m1):
            for j in range(m2):
                answer += number[num1[i]] * number[num2[j]] * 10 ** (m1+m2-i-j-2)
        return str(answer)