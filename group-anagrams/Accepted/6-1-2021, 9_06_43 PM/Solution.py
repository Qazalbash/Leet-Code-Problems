// https://leetcode.com/problems/group-anagrams

class Solution:
#     def merge(self, A, L, R):
#         nL, nR, i, j, k = len(L), len(R), 0, 0, 0
#         while i < nL and j < nR:
#             if L[i] <= R[j]:
#                 A[k] = L[i]
#                 i += 1
#             else:
#                 A[k] = R[j]
#                 j += 1
#             k += 1
#         while i < nL:
#             A[k] = L[i]
#             i += 1
#             k += 1
#         while j < nR:
#             A[k] = R[j]
#             j += 1
#             k += 1

#     def mergeSort(self, A):
#         n = len(A)
#         if n > 1:
#             mid = n // 2
#             L, R = A[:mid], A[mid:]
#             self.mergeSort(L)
#             self.mergeSort(R)
#             self.merge(A, L, R)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for i in strs:
            j = "".join(sorted(i))
            ana[j] = ana.get(j, []) + [i]
        return [ana[i] for i in ana.keys()]
        # return ana
        