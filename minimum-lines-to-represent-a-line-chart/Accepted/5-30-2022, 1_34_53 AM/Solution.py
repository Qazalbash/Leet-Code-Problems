// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) < 2:
            return 0
        count = 1
        stockPrices = sorted(stockPrices, key=lambda k: k[0])
        for i in range(len(stockPrices)-2):
            x1, y1 = stockPrices[i]
            x2, y2 = stockPrices[i+1]
            x3, y3 = stockPrices[i+2]
            
            # area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
            count += x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0
        return count