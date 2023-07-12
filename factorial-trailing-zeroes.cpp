// https://leetcode.com/problems/factorial-trailing-zeroes

class Solution {
public:
    int trailingZeroes(int n) {
        int twos = 0, fives = 0;
        while(n) {
            int k = n;
            while (k % 2 == 0) {
                ++twos;
                k >>= 1;
            }
            while (k % 5 == 0) {
                ++fives;
                k /= 5;
            }
            --n;
        }
        return min(twos, fives);
    }
};