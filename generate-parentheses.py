// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        return ['(' + left + ')' + right
                for i in range(n)
                for left in self.generateParenthesis(i)
                for right in self.generateParenthesis(n - i - 1)]