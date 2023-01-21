// https://leetcode.com/problems/rectangle-area

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        height_b = by2 - by1
        breath_b = bx2 - bx1
        
        height_a = ay2 - ay1
        breath_a = ax2 - ax1
        
        A1 = height_a * breath_a
        A2 = height_b * breath_b
        
        sx2 = ax2 * (ax2 < bx2) + bx2 * (ax2 >= bx2)
        sy2 = ay2 * (ay2 < by2) + by2 * (ay2 >= by2)
        
        sx1 = ax1 * (ax1 > bx1) + bx1 * (ax1 <= bx1)
        sy1 = ay1 * (ay1 > by1) + by1 * (ay1 <= by1)
        
        height_s = sy2 - sy1
        breath_s = sx2 - sx1
        
        
        A12 = height_s * breath_s if height_s > 0 and breath_s > 0 else 0
        
        print(A12)
        
        return A1 + A2 - A12