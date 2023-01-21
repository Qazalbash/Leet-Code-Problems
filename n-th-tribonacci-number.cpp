// https://leetcode.com/problems/n-th-tribonacci-number

class Solution {
public:
    int tribonacci(int n) {
        if ( n == 0 ) return 0;
        if( n < 3 ) return 1;
        int nums[n + 1];
        nums[0] = 0;
        nums[1] = 1;
        nums[2] = 1;
        for(int i = 3; i <= n; i++ )
            nums[i] = nums[i-3] + nums[i-2] + nums[i-1];
        return nums[n];
        
    }
};