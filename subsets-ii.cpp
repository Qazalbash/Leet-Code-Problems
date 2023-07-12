// https://leetcode.com/problems/subsets-ii

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        const int size = nums.size();
        vector<int> r;
        set<vector<int>> subsets = {{}};
        int index = 1;
        const int max_index = 1 << size;
        while (index < max_index) {
            int counter = 0, temp = index;
            
            while (counter < size) {
                if (temp & 0x1) {
                    r.push_back(nums[counter]);
                }
                
                temp >>= 1;
                ++counter;
            }

            subsets.insert(r);
            r.clear();
            ++index;
        }

        vector<vector<int>> ans;
        ans.assign(subsets.begin(), subsets.end());
        return ans;
    }
};