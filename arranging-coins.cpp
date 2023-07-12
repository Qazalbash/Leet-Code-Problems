// https://leetcode.com/problems/arranging-coins

class Solution {
public:
    int arrangeCoins(int n) {
        const size_t eight_n = (size_t)n << 3;
        const float d = sqrtf(eight_n + 1ul);
        const size_t k = (-1.0f + d) / 2ul;
        return (((k*k + k) >> 1) > n) ? k - 1 : k;
    }
};