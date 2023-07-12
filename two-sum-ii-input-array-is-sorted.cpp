// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        const size_t n = numbers.size();
        int left, right, search, mid;
        for(int i = 0; i < n; ++i) {
            search = target - numbers[i];
            left = 0, right = n - 1;
            while (left <= right) {
                mid = (left + right) >> 1;
                if (numbers[mid] == search && i != mid) return { i + 1, mid + 1 };
                if (numbers[mid] <= search) left = mid + 1;
                else right = mid - 1;
            }
        }
        return {-1,-1};
    }
};