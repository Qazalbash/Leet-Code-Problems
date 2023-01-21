// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ana = {"(":1, "{":2, "[":3, ")":1, "}":2, "]":3}
        try:
            for i in s:
                if i in "({[":
                    stack.append(ana[i])
                elif stack[-1] == ana[i]:
                    stack.pop()
                else:
                    return False
        except:
            return False
        return len(stack) == 0  