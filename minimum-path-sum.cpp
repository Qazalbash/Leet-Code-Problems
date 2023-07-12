// https://leetcode.com/problems/minimum-path-sum

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int i, j;
        const int m = grid.size(), n = grid[0].size();

        for(i = 0 ; i < m ; ++i) {
            for(j = 0 ; j < n ; ++j) {
                if      (i == 0 && j == 0) continue;
                else if (i == 0 && j > 0)  grid[i][j] += grid[i][j-1];
                else if (j == 0 && i > 0)  grid[i][j] += grid[i-1][j];
                else                       grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
            }
        }

        return grid[m-1][n-1];
    }
};