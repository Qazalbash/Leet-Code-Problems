// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]
        # c = a * (len(a) > len(b)) + b * (len(a) <= len(b))
        # d = b * (len(a) > len(b)) + a * (len(a) <= len(b))
        # A = [int(i) for i in c[::-1]] + [0]
        # B = [int(i) for i in d[::-1]] + [0]
        # for i in range(len(d)):
        #     if A[i] + B[i] == 1:
        #         A[i] = 1
        #     elif A[i] + B[i] == 2:
        #         A[i] = 0
        #         A[i+1] = A[i+1] + 1
        #     elif A[i] + B[i] == 3:
        #         A[i] = 1
        #         A[i+1] = A[i+1] + 1
        # if 2 in A:
        #     for i in range(len(A)):
        #         if A[i] == 2:
        #             A[i] = 0
        #             A[i+1] = A[i+1] + 1
        # return "".join([str(i) for i in A[::-1]])