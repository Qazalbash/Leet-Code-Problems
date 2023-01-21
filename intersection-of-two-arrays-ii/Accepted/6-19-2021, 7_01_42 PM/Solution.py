// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1,d2={i:0 for i in nums2},{i:0 for i in nums1}
        for i in nums1:
            d1[i]=d1.get(i,0)+1
        for j in nums2:
            d2[j]=d2.get(j,0)+1
        r=[]
        for k,v in d1.items():
            for h in range(min(v,d2[k])):
                r.append(k)
        return r