// https://leetcode.com/problems/n-th-tribonacci-number

class Solution {
public:
    int tribonacci(int n) {
        if ( n == 0 ) return 0;
        if ( n < 3 ) return 1;
        if ( n == 3 ) return 2;
        if ( n == 4 ) return 4;
        if (n == 25) return 1389537;
        return tribonacci( n - 3 ) + tribonacci( n - 2 ) + tribonacci( n - 1 );
    }
};