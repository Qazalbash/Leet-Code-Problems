// https://leetcode.com/problems/search-a-2d-matrix

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int left = 0, right = matrix.size() - 1, mid;
        while (left <= right) {
            mid = (left + right) >> 1;
            if (matrix[mid][0] == target) return true;
            if (matrix[mid][0] > target) right = mid - 1;
            else left = mid + 1;
        }

        // cout << left << " " << right << endl;

        if (right < 0) return false;

        const int row = right;
        left = 0;
        right = matrix[0].size() - 1;

        while (left <= right) {
            mid = (left + right) >> 1;
            if (matrix[row][mid] == target) return true;
            else if (matrix[row][mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        
        return false;
    }
};