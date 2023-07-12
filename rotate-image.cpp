// https://leetcode.com/problems/rotate-image

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        const int n = matrix.size();
        int i, j;
        for (i = 0; i < n; ++i) {
            for (j = i + 1; j < n; ++j) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        for (i = 0; i < n; ++i) {
            for (j = n >> 1; j < n; ++j) {
                swap(matrix[i][j], matrix[i][n-j-1]);
            }
        }
    }
};