// https://leetcode.com/problems/two-sum

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i=0;i<size(nums);i++)
            for(int j=i+1;j<size(nums);j++)
                if(nums[i]+nums[j]==target)
                    return {i,j};
    return {-1,-1};
    }
};