// https://leetcode.com/problems/rectangle-overlap

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax1, ay1, ax2, ay2 = rec1
        bx1, by1, bx2, by2 = rec2
        
        sx2 = ax2 * (ax2 < bx2) + bx2 * (ax2 >= bx2)
        sy2 = ay2 * (ay2 < by2) + by2 * (ay2 >= by2)
        
        sx1 = ax1 * (ax1 > bx1) + bx1 * (ax1 <= bx1)
        sy1 = ay1 * (ay1 > by1) + by1 * (ay1 <= by1)
        
        height_s = sy2 - sy1
        breath_s = sx2 - sx1
        
        return True if height_s > 0 and breath_s > 0 else False