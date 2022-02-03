class Solution:

    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        A, nL, nR, i, j, k = nums1 + nums2, len(nums1), len(nums2), 0, 0, 0
        while i < nL and j < nR:
            if nums1[i] <= nums2[j]:
                A[k] = nums1[i]
                i += 1
            else:
                A[k] = nums2[j]
                j += 1
            k += 1
        while i < nL:
            A[k] = nums1[i]
            i += 1
            k += 1
        while j < nR:
            A[k] = nums2[j]
            j += 1
            k += 1
        a = len(A)
        if len(A) % 2 == 1:
            return A[int(a / 2)]
        else:
            return (A[int(a / 2) - 1] + A[int(a / 2)]) / 2
