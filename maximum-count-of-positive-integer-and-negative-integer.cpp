// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer

class Solution {
public:
    int maximumCount(vector<int>& nums) {
        const int n = nums.size();
        int mid, left = 0, right = n - 1;
        while (left <= right) {
            mid = (left + right) >> 1;
            if (nums[mid] >= 0) right = mid - 1;
            else left = mid + 1;
        }
        const int negatives = right + 1;
        left = 0, right = n - 1;
        while (left <= right) {
            mid = (left + right) >> 1;
            if (nums[mid] <= 0) left = mid + 1;
            else right = mid - 1;
        }
        const int positives = n - left;
        return max(negatives, positives);
    }
};