// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''
        for j in s:
            if j.isalnum():
                a+=j.lower()
        for i in range(len(a)):
            if a[i]!=a[-i-1]:
                return False
        return True
            