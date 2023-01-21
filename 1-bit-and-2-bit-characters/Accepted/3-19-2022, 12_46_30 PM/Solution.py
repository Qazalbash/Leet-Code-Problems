// https://leetcode.com/problems/1-bit-and-2-bit-characters

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 0:
            return False
        elif len(bits) == 1:
            return bits[0] == 0
        elif bits[:2] == [1,0] or bits[:2] == [1,1]:
            return self.isOneBitCharacter(bits[2:])
        elif bits[0] == 0:
            return self.isOneBitCharacter(bits[1:])