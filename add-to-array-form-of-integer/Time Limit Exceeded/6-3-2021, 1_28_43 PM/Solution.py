// https://leetcode.com/problems/add-to-array-form-of-integer

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # n = sum([num[i]*10**(len(num)-i-1) for i in range(len(num))])
        # return [int(i) for i in str(n+k)]
        K = [int(i) for i in str(k)]
        carry=0
        a,b=len(num)-1,len(K)-1
        while a>-1 or b>-1 or carry:
            if a>-1 and b>-1:
                w = num[a]+K[b]+carry
                num[a]=w%10
                carry=int(w//10)
                a-=1
                b-=1
            elif a>-1:
                w = num[a]+carry
                num[a]=w%10
                carry=int(w//10)
                a-=1
                
#         for j in range(len(K)):
#             a = num[-j-1]+K[-j-1]+carry
#             num[-j-1]=a%10
#             carry=int(a//10)
        return num