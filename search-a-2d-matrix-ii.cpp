// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int left, right, mid;
        const int n = matrix.size();

        for(int row = 0; row < n; ++row){
            left = 0;
            right = matrix[0].size() - 1;
            while (left <= right) {
                mid = (left + right) >> 1;
                if (matrix[row][mid] == target) return true;
                else if (matrix[row][mid] < target) left = mid + 1;
                else right = mid - 1;
            }
        }

        return false;
    }
};