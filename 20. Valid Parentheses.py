class Solution:

    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        ana = {")": "(", "}": "{", "]": "["}
        try:
            for i in s:
                if i in "({[":
                    stack.append(i)
                elif stack[-1] == ana[i]:
                    stack.pop()
                else:
                    return False
        except:
            return False
        return len(stack) == 0
