// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]=digits[-1]+1
        index=len(digits)-1
        while digits[index]>9 and index>0:
            x=digits[index]
            digits[index-1],digits[index]=digits[index-1]+int(x/10),x%10
            index-=1
        return [int(digits[0]/10)]*(digits[0]>9)+[digits[0]%10]+digits[1:]