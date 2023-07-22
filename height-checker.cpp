// https://leetcode.com/problems/height-checker

class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> expected(heights.begin(), heights.end());
        sort(expected.begin(), expected.end());
        int count = 0;
        const int n = heights.size();
        for(int i=0; i<n; ++i) {
            if (heights[i] != expected[i]) {
                ++count;
            }
        }
        return count;
    }
};