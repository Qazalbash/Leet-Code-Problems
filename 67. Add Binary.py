class Solution:

    def addBinary(self, a: str, b: str) -> str:
        r = int(a, 2) + int(b, 2)
        return str(bin(r))[2:]
