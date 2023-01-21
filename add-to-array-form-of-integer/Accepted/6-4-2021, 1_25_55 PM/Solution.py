// https://leetcode.com/problems/add-to-array-form-of-integer

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # n = sum([num[i]*10**(len(num)-i-1) for i in range(len(num))])
        # return [int(i) for i in str(n+k)]
        
        K = [int(i) for i in str(k)]
        if len(num)<len(K): num, K = K, num
        a,b,c=len(num)-1,len(K)-1,0
        while a>-1 or b>-1:
            p1=a>-1 and b>-1 or a>-1
            p2=a>-1 and b>-1 or b>-1
            w=c+num[a]*p1+K[b]*p2
            num[a]=w%10
            c=int(w//10)
            a-=p1
            b-=p2
        return [c]+num if c>0 else num