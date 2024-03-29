// https://leetcode.com/problems/substring-with-concatenation-of-all-words

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        m = len(words[0])
        _s_ = len(s)
        r = []
        i = 0

        while i + m * n <= _s_:
            s_ = [s[k:k + m] for k in range(i, i + m * n, m)]
            for w in words:
                if w in s_:
                    s_.remove(w)
                else:
                    break
            if not s_:
                r.append(i)
            i += 1

        return r