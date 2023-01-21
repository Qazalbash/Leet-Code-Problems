// https://leetcode.com/problems/n-th-tribonacci-number

class Solution {
public:
    int tribonacci(int n) {
        if ( n <= 0 ) return 0;
        if ( n < 3 ) return 1;
        return tribonacci( n - 3 ) + tribonacci( n - 2 ) + tribonacci( n - 1 );
    }
};