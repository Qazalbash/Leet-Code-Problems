class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = [i for i in str(x)]
        return num == num[::-1]
