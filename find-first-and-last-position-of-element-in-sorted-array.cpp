// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        
        if (nums.size() == 0ul) {
            const vector<int> result = {-1, -1};
            return result;
        }
        
        int position;
        int left = 0;
        int right = nums.size() - 1;
        int middle;
        
        while (left <= right) {
            middle = (left + right) >> 1;
            if (nums[middle] == target) {
                position = middle;
                break;
            } else if (nums[middle] > target) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        
        if (left > right) {
            const vector<int> result = {-1, -1};
            return result;
        }
        
        left = position;
        right = position;

        while (left >= 0 && nums[left] == target) --left;
        while (right < nums.size() && nums[right] == target) ++right;

        ++left;
        --right;

        const vector<int> result = {left, right};

        return result;
    }
};