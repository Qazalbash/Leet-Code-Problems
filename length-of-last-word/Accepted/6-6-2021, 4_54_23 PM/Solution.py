// https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = ""
        s=s.strip(" ")
        for i in s:
            last_word = (last_word+i)*(i!=" ")+""*(i==" ")
        return len(last_word)