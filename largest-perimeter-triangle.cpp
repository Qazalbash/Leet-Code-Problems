// https://leetcode.com/problems/largest-perimeter-triangle

class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end(), [](const int a, const int b) { return a > b; });
        int i, j, k;
        const int n = nums.size();
        for(i = 0; i + 2 < n; ++i) {
            const int a = nums[i];
            const int b = nums[i + 1];
            const int c = nums[i + 2];
            if (forms_triangle(a, b, c)) {
                return a + b + c;
            }
        }
        return 0;
    }

private:
    bool forms_triangle(const int a, const int b, const int c) {
        return (
            a + b > c &&
            a + c > b &&
            b + c > a
        );
    }
};