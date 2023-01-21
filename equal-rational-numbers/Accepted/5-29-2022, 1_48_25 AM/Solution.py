// https://leetcode.com/problems/equal-rational-numbers

class frac:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __add__(self, other):
        a = self.num * other.denom + other.num * self.denom
        b = self.denom * other.denom
        gcd = self.hcf(a, b)

        self.num = a // gcd
        self.denom = b // gcd
        return self

    def __eq__(self, other):
        return (self.num == other.num) and (self.denom == other.denom)

    def hcf(self, x, y):
        while y:
            x, y = y, x % y
        return x


class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def geo_sum(num: str) -> frac:
            if "(" in num:
                parts = num.split(".")

                rp = parts[-1].replace(")", "")
                rp = rp.split("(")

                parts.pop()
                parts.extend(rp)

                n = len(parts[1])
                m = len(parts[2])

                if parts[1] == "":
                    parts[1] = "0"

                p = (
                    frac(int(parts[0]), 1)
                    + frac(int(parts[1]), 10**n)
                    + frac(int(parts[2]), 10 ** (n + m) - 10**n)
                )
                return p

            elif "." in num:
                parts = num.split(".")
                n = len(parts[1])
                if parts[1] == "":
                    parts[1] = "0"
                return frac(int(parts[0]), 1) + frac(int(parts[1]), 10**n)
            else:
                return frac(int(num), 1)

        return geo_sum(s) == geo_sum(t)