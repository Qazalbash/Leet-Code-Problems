class Solution:
    def clumsy(self, n: int) -> int:
        exp, j = "", 0
        for i in range(n, 1, -1):
            exp += str(i)
            if j % 4 == 0:
                exp += "*"
            elif j % 4 == 1:
                exp += "//"
            elif j % 4 == 2:
                exp += "+"
            else:
                exp += "-"
            j += 1
        return int(eval(exp + "1"))
