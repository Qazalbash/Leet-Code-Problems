// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]=digits[-1]+1
        i=len(digits)-1
        while digits[i]>9 and i>0:
            x=digits[i]
            digits[i-1],digits[i]=digits[i-1]+int(x/10),x%10
            i-=1
        return [int(digits[0]/10)]*(digits[0]>9)+[digits[0]%10]+digits[1:]