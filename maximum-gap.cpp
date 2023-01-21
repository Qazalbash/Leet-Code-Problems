// https://leetcode.com/problems/maximum-gap

class Solution {
public:
    int maximumGap(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        long unsigned int i = 0;
        int d = 0;
        for(;i+1<nums.size(); i++){
            if (d + nums[i] < nums[i+1]) d = nums[i+1] - nums[i];
        }
        return d;
    }
};