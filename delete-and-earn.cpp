// https://leetcode.com/problems/delete-and-earn

class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        const size_t size = nums.size();
        if (size == 0ul) { return 0; }
        const int max_val = *max_element(nums.begin(), nums.end());
        vector<int> total(max_val + 1, 0);
        for(const int i : nums) {
            total[i] += i;
        }
        int first = total[0];
        int second = max(total[0], total[1]);
        for(size_t i = 2ul; i < max_val + 1; ++i) {
            const int dp = max(first + total[i], second);
            first = second;
            second = dp;
        }
        return second;
    }
};