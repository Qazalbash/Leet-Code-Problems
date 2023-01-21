// https://leetcode.com/problems/self-dividing-numbers

class Solution:
    import math
    @staticmethod
    def digits(num: int)->List[int]:
        return [
            (num % (10 ** (i + 1)) - num % (10 ** i)) // (10 ** i) 
            for i in range(int(math.log10(num))+1)
        ]
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing_numbers = []
        for num in range(left, right + 1):
            keep = True
            for d in self.digits(num):
                if d == 0:
                    keep = False
                else:
                    keep &= num % d == 0
            if keep:
                self_dividing_numbers.append(num)
        return self_dividing_numbers