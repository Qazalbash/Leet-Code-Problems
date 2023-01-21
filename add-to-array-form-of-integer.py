// https://leetcode.com/problems/add-to-array-form-of-integer

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = sum([num[i]*10**(len(num)-i-1) for i in range(len(num))])
        return [int(i) for i in str(n+k)]