// https://leetcode.com/problems/house-robber

class Solution {
public:
    int rob(vector<int>& nums) {
        int a = 0, b = 0;
        for (const int n : nums) {
            const int dp = max(a, b + n);
            b = a;
            a = dp;
        }
        return a;
    }
};