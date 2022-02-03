class Solution:

    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        K = [int(i) for i in str(k)]
        carry = 0
        if len(num) < len(K):
            num, K = K, num
        a, b = len(num) - 1, len(K) - 1
        while a > -1 or b > -1:
            w = carry
            if a > -1 and b > -1:
                w += num[a] + K[b]
            elif a > -1:
                w += num[a]
            elif b > -1:
                w += K[b]
            num[a] = w % 10
            carry = int(w // 10)
            a -= a > -1 and b > -1 or a > -1
            b -= a > -1 and b > -1 or b > -1
        return [carry] + num if carry > 0 else num
