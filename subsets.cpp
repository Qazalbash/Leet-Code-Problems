// https://leetcode.com/problems/subsets

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        const int size = nums.size();
        vector<vector<int>> subsets;
        vector<int> r;
        subsets.push_back(r);
        int index = 1;
        const int max_index = 1 << size;
        while (index < max_index) {
            int counter = 0;
            int temp = index;
            while (counter < size) {
                if (temp & 0x1) {
                    r.push_back(nums[counter]);
                }
                temp >>= 1;
                ++counter;
            }
            subsets.push_back(r);
            r.clear();
            ++index;
        }
        return subsets;
    }
};