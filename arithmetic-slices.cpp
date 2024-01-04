// https://leetcode.com/problems/arithmetic-slices

class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        const size_t n = nums.size();
        
        if (n < 3) { return 0; }


        int d = 0, count = 0;

        size_t i = 2;

        while(i < n) {
            if (nums[i] + nums[i-2] == 2 * nums[i-1]) {
                d = nums[i] - nums[i-1];
                ++i;
                count = 1;
                break;
            } else {
                ++i;
            }
        }

        int chunk = 1;
        
        for(; i < n; ++i) {
            // cout << "right = " << right << endl;
            if (d + nums[i-1] == nums[i]) {
                ++chunk;
                count += chunk;
            } else {
                d = nums[i] - nums[i-1];
                chunk = 0;
            }
        }

        // count += (((right - left) * (right - left - 1)) >> 1);

        // cout << left << " " << right << endl;

        return count;
    }
};