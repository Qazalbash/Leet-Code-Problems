// https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return [k*k for k in nums]
        
        i = n - 1
        
        if nums[0] >= 0 and nums[1] >= 0:
            i = 0
        elif nums[-2] < 0 and nums[-1] < 0:
            i = n - 1
        else:
            for p in range(n-1):
                if nums[p] < 0 and nums[p+1] >= 0:
                    i = p
                    break
        
        final = []
        j = i + 1
        
        while i >= 0 and j < n:
            a,b = nums[i]**2, nums[j]**2
            if a <= b:
                final.append(a)
                i -= 1
            else:
                final.append(b)
                j += 1
        
        if i >= 0:
            final.extend([k*k for k in nums[:i+1][::-1]])
        if j < n:
            final.extend([k*k for k in nums[j:]])
        return final
            