// https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = 0
        s=s.strip(" ")
        for i in s:
            last_word = (last_word+1)*(i!=" ")
        return last_word