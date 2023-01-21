// https://leetcode.com/problems/reverse-integer

#include <cmath>
class Solution {
public:
    int reverse(int x) {
        if(x==0 || pow(2,31)-1>x>pow(2,31)){return 0;};
        int sign=(x>0)-(x<0), N=0;
        x=abs(x);
        int m = floor(log10(x)),k=0;
        do{
            N+=pow(10,m-k)*(floor(x/pow(10,k))-10*floor(x/pow(10,k+1)));
            k++;
        } while(-pow(2,31)<=N<=pow(2,31)-1);
        // for(int k=0;k<=m+1;k++){
        //     if(-pow(2,31)<=N<=pow(2,31)-1){
        //         N+=pow(10,m-k)*(floor(x/pow(10,k))-10*floor(x/pow(10,k+1)));
        //     };
        // }
        return N*sign*(-pow(2,31)<=N<=pow(2,31)-1);
    }
};