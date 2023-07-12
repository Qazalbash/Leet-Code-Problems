// https://leetcode.com/problems/unique-paths

class Solution {
public:
    int uniquePaths(int m, int n) {
        int grid[m][n];
        for(int i = 0 ; i < m ; ++i) {
            for(int j = 0 ; j < n ; ++j) {
                grid[i][j] = 0;
            }
        }
        grid[0][0] = 1;

        for(int i = 0 ; i < m ; ++i) {
            for(int j = 0 ; j < n ; ++j) {
                if (i + 1 < m) {
                    grid[i+1][j] += grid[i][j];
                }
                if (j + 1 < n) {
                    grid[i][j+1] += grid[i][j];
                }
            }
        }

       
        return grid[m-1][n-1];
    }
};