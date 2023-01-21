// https://leetcode.com/problems/add-to-array-form-of-integer

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # n = sum([num[i]*10**(len(num)-i-1) for i in range(len(num))])
        # return [int(i) for i in str(n+k)]
        
        # K = [int(i) for i in str(k)[::-1]]
        # num = num[::-1]
        # if len(num)<len(K):
        #     num, K = K, num
        # carry=0
        # b=0
        # a=0
        # while a<len(num) or b<len(K):
        #     if a<len(num) and b<len(K):
        #         w = num[a]+K[b]+carry
        #         num[a]=w%10
        #         carry=int(w//10)
        #         a+=1
        #         b+=1
        #     elif a<len(num) and b>=len(K):
        #         w = num[a]+carry
        #         num[a]=w%10
        #         carry=int(w//10)
        #         a+=1
        #     elif b<len(K) and a>=len(num):
        #         w = K[b]+carry
        #         num[a]=w%10
        #         carry=int(w//10)
        #         b+=1
        # return [carry]+num[::-1] if carry>0 else num[::-1]
        
        K = [int(i) for i in str(k)]
        carry=0
        if len(num)<len(K):
            num, K = K, num
        a,b=len(num)-1,len(K)-1
        while a>-1 or b>-1:
            p1=a>-1 and b>-1 or a>-1
            p2=a>-1 and b>-1 or b>-1
            w=carry+num[a]*p1+K[b]*p2
            num[a]=w%10
            carry=int(w//10)
            a-=p1
            b-=p2
        return [carry]+num if carry>0 else num