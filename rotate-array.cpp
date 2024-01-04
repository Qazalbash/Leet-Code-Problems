// https://leetcode.com/problems/rotate-array

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        const int n = nums.size();
        k %= n;
        vector<int> num;
        num.reserve(n);
        num.insert(num.end(), nums.end() - k, nums.end());
        num.insert(num.end(), nums.begin(), nums.end() - k);
        nums = num;
    }
};