// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        
        comb = list(self.button(digits[-1]))
        n -= 2
        while n >= 0:
            comb = [j+i for i in comb for j in self.button(digits[n])]
            n -= 1
        return comb

    def button(self, n: str) -> str:
        if n == '2':
            return "abc"
        elif n == '3':
            return "def"
        elif n == '4':
            return "ghi"
        elif n == '5':
            return "jkl"
        elif n == '6':
            return "mno"
        elif n == '7':
            return "pqrs"
        elif n == '8':
            return "tuv"
        elif n == '9':
            return "wxyz"
        return ""