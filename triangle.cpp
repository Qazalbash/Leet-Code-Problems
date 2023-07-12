// https://leetcode.com/problems/triangle

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        const size_t n = triangle.size();
        int memo[n][n];
        
        for (int i = 0; i < n ; ++i) {
            memo[n-1][i] = triangle[n-1][i];
        }

        for (int i = n - 2; 0 <= i ; --i) {
            for (int j = 0; j <= i ; ++j) {
                memo[i][j] = triangle[i][j] + min(memo[i+1][j], memo[i+1][j+1]);
            }
        }
        return memo[0][0];
    }
};