// https://leetcode.com/problems/n-th-tribonacci-number

class Solution {
public:
    int tribonacci(int n) {
        if(n<3) {
            return (3*n - n * n)/2;
        };
        return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3);
    }
};