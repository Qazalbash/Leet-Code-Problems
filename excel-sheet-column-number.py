// https://leetcode.com/problems/excel-sheet-column-number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = 0
        k = len(columnTitle) - 1
        for i in columnTitle:
            n += (ord(i) - 64) * (26 ** k)
            k -= 1
        return n